from database.DataBase import Database
import json
from utils.UtilsService import exclude_fields, handle_exceptions, validate_required_fields_habitacion


class ServicioHabitacion:
    def __init__(self):
        self.bd = Database()

    @handle_exceptions
    def insert_habitacion(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields_habitacion(data, "insert")
        id_hotel = data['id_hotel']
        costo = data['costo_habitacion']
        ubicacion = data['ubicacion']
        impuesto = data['impuesto']
        tipo = data['tipo']
        capacidad = data['capacidad']
        sql_insert = """INSERT INTO tbl_habitaciones (id_hotel, costo, ubicacion,capacidad, impuesto, tipo, activo, estado)
                        VALUES (%s, %s, %s, %s, %s, 1, 1);"""
        self.bd.statement(sql_insert, (id_hotel, costo, ubicacion, capacidad, impuesto, tipo))
        return {"statusCode": 201, "body": data}

    @handle_exceptions
    def select_habitacion(self) -> dict:
        sql_select = """select id_habitaciones,  id_hotel, nombre_hotel, ciudad,
                               direccion_hotel, th.costo, ubicacion,capacidad, 
                               impuesto, tth.descripcion as tipo_habitacion,est.descripcion as estado 
                        from tbl_habitaciones th 
                        inner join tbl_hoteles on tbl_hoteles.id_hoteles = th.id_hotel
                        inner join tbl_tipo_habitacion tth ON tth.id_tipo_habitacion  = th.tipo
                        inner join tbl_estado est ON est.id_estado  = th.estado"""
        habitaciones = self.bd.select(sql_select)
        return {"statusCode": 200, "data": exclude_fields(habitaciones)}

    @handle_exceptions
    def deactivate_habitacion(self, id: int) -> dict:
        id_habitacion = self._select_habitacion_by_id(id)
        if id_habitacion:
            sql_update = """UPDATE tbl_habitaciones
                            SET activo = 0, estado = 2
                            WHERE id_habitaciones = %s;"""
            self.bd.statement(sql_update, (id,))
            return {"statusCode": 204, "data": "deactivate successful"}
        else:
            return {"statusCode": 404, "data": "Habitacion Not Found"}

    @handle_exceptions
    def update_habitacion(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields_habitacion(data, "update")
        id_habitacion = data['id_habitacion']
        id_hotel = data['id_hotel']
        costo = data['costo_habitacion']
        ubicacion = data['ubicacion']
        impuesto = data['impuesto']
        tipo = data['tipo']
        hotel = self._select_hotel_by_id(id_hotel, id_habitacion)

        if hotel:
            sql_update = """UPDATE tbl_habitaciones
                            SET id_hotel = %s, costo = %s, ubicacion = %s , impuesto = %s, tipo = %s
                            WHERE id_habitaciones = %s and activo = 1;"""

            self.bd.statement(sql_update, (id_hotel, costo, ubicacion, impuesto, tipo, id_habitacion))
            return {"statusCode": 204, "data": data}

        return {"statusCode": 404, "data": "Hotel Not Found Or Habitacion Inactive "}

    def _select_habitacion_by_id(self, id: int) -> bool:
        sql_select = f"""SELECT id_habitaciones 
                         FROM tbl_habitaciones 
                         WHERE id_habitaciones= {id} 
                         and activo = 1"""
        habitaciones = self.bd.select(sql_select)
        return False if len(habitaciones) == 0 else True

    def _select_hotel_by_id(self, id: int, id_habitacion: int) -> bool:
        sql_select = f"""SELECT id_hoteles FROM tbl_hoteles
                         INNER JOIN tbl_habitaciones
                         ON tbl_habitaciones.id_hotel = tbl_hoteles.id_hoteles
                        WHERE id_hoteles = {id} and tbl_hoteles.activo = 1 
                        and tbl_habitaciones.activo = 1
                        and  tbl_habitaciones.id_habitaciones = {id_habitacion}"""
        hotels = self.bd.select(sql_select)
        return False if len(hotels) == 0 else True
