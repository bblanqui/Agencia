import datetime
import uuid
from database.DataBase import Database
import json
from utils.UtilsService import handle_exceptions, validate_required_fields_reserva
from servicio.ServicioSendMail import send_mail


class ServicioReservaHotel:
    def __init__(self):
        self.bd = Database()

    @handle_exceptions
    def insert_reserva(self, event: dict) -> dict:
        reserva = uuid.uuid4()
        numero_reserva = str(reserva)
        data = json.loads(event['body'])
        validate_required_fields_reserva(data)
        id_habitacion = data["id_habitacion"]
        nombre_reserva = data["nombre_reserva"]
        fecha_entrada = data["fecha_entrada"]
        fecha_salida = data["fecha_salida"]
        cantidad_persona = data["cantidad_persona"]
        correo_cliente = data["correo_cliente"]
        telefono_cliente = data["telefono_cliente"]
        nombre_contacto_emergencia = data["nombre_contacto_emergencia"]
        telefono_contacto_emergencia = data["telefono_contacto_emergencia"]
        disponible = self._seach_disponible(fecha_entrada, fecha_salida, cantidad_persona, id_habitacion)
        if len(disponible) > 0:
            sql_select = f"""INSERT INTO Agencia.tbl_reserva
                            (
                                id_habitacion,
                                nombre_reserva,
                                fecha_entrada,
                                fecha_salida,
                                cantidad_persona,
                                ciudad_destino,
                                fecha_reserva,
                                correo_cliente,
                                telefono_cliente,
                                nombre_contacto_emergencia,
                                telefono_contacto_emergencia,
                                numero_reserva
                            )
                            VALUES
                            (
                               {id_habitacion}, 
                               '{nombre_reserva}',           
                               '{fecha_entrada}',          
                               '{fecha_salida}',  
                                {cantidad_persona},           
                                '{disponible[0]["ciudad"]}', 
                                 '{datetime.datetime.now()}',          
                                '{correo_cliente}',         
                                '{telefono_cliente}',          
                                '{nombre_contacto_emergencia}',             
                                '{telefono_contacto_emergencia}',
                                '{numero_reserva}'       
                            );"""
            self.bd.statement(sql_select)

            send_mail(cantidad_persona, disponible[0]["costo"],
                      disponible[0]["impuesto"], nombre_reserva,
                      disponible[0]["direccion_hotel"],
                      disponible[0]["ciudad"],
                      fecha_entrada,
                      fecha_salida,
                      numero_reserva,
                      disponible[0]["nombre_hotel"],
                      )
            return {"statusCode": 200, "data": data}
        return {"statusCode": 401, "data": "habitación no disponible o cantidad de huesped superado"}

    @handle_exceptions
    def _seach_disponible(self, fecha_entrada: str, fecha_salida: str, cantidad_persona: int,
                          id_habitacion: int) -> dict:
        sql_select = f"""SELECT
                            H.ciudad, HA.costo, HA.impuesto,
                            H.direccion_hotel, H.nombre_hotel
                        FROM
                            Agencia.tbl_hoteles AS H
                        INNER JOIN
                            Agencia.tbl_habitaciones AS HA
                        ON
                            H.id_hoteles = HA.id_hotel
                        LEFT JOIN
                            Agencia.tbl_reserva AS R
                        ON
                            HA.id_habitaciones = R.id_habitacion
                            AND (
                                ('{fecha_entrada}' BETWEEN R.fecha_entrada AND R.fecha_salida)
                                OR
                                ('{fecha_salida}' BETWEEN R.fecha_entrada AND R.fecha_salida)
                            )
                        INNER JOIN
                            tbl_tipo_habitacion AS TTH
                        ON
                            TTH.id_tipo_habitacion = HA.tipo
                        WHERE
                            H.activo = 1
                            AND HA.activo=1
                            AND R.id_reserva IS NULL
                            AND HA.capacidad >= {cantidad_persona}
                            AND HA.id_habitaciones = {id_habitacion}
                        ORDER BY H.id_hoteles;"""

        habitaciones = self.bd.select(sql_select)
        return habitaciones
