from database.DataBase import Database
import json
from utils.UtilsService import exclude_fields, handle_exceptions, validate_required_fields_search


class ServicioSearchHotel:
    def __init__(self):
        self.bd = Database()

    @handle_exceptions
    def seach_hotel(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields_search(data)
        fecha_entrada = data["fecha_entrada"]
        fecha_salida = data["fecha_salida"]
        cantidad_persona = data["cantidad_persona"]
        ciudad = data["ciudad"]
        sql_select = f"""SELECT
                            H.id_hoteles,
                            H.nombre_hotel,
                            H.direccion_hotel,
                            H.ciudad,
                            HA.id_habitaciones AS id_habitacion,
                            HA.costo,
                            HA.ubicacion,
                            HA.impuesto,
                            TTH.descripcion,
                            HA.capacidad
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
                            AND R.id_reserva IS NULL
                            AND H.ciudad LIKE '%{ciudad}%' 
                            AND HA.capacidad >= {cantidad_persona}
                        ORDER BY H.id_hoteles;"""
        hoteles = self.bd.select(sql_select)
        return {"statusCode": 200, "data": exclude_fields(hoteles)}

