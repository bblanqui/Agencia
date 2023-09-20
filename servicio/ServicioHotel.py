from database.DataBase import Database
import json
from utils.UtilsService import exclude_fields, handle_exceptions, validate_required_fields


class ServicioHotel:
    def __init__(self):
        self.bd = Database()

    @handle_exceptions
    def insert_hotel(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields(data, "insert")
        nombre_hotel = data['nombre_hotel']
        direccion_hotel = data['direccion_hotel']
        ciudad = data['ciudad']
        sql_insert = """INSERT INTO tbl_hoteles (nombre_hotel, direccion_hotel, activo, ciudad)
                        VALUES (%s, %s, 1, %s);"""
        self.bd.statement(sql_insert, (nombre_hotel, direccion_hotel, ciudad))
        return {"statusCode": 201, "body": data}

    @handle_exceptions
    def select_hotel(self) -> dict:
        sql_select = """SELECT id_hoteles, nombre_hotel, direccion_hotel, ciudad FROM tbl_hoteles WHERE activo = 1;"""
        hotels = self.bd.select(sql_select)
        return {"statusCode": 200, "data": exclude_fields(hotels)}

    @handle_exceptions
    def deactivate_hotel(self, id: int) -> dict:
        id_hotel = self._select_hotel_by_id(id)
        if id_hotel:
            sql_update = """UPDATE tbl_hoteles SET activo = 0 WHERE id_hoteles = %s;"""
            self.bd.statement(sql_update, (id,))
            return {"statusCode": 204, "data": "deactivate successful"}
        else:
            return {"statusCode": 404, "data": "Hotel Not Found"}

    @handle_exceptions
    def update_hotel(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields(data, "update")
        id = data["id"]
        nombre = data["nombre_hotel"]
        direccion_hotel = data["direccion_hotel"]
        ciudad = data["ciudad"]
        sql_update = """UPDATE tbl_hoteles
                        SET nombre_hotel = %s, direccion_hotel = %s, ciudad = %s
                        WHERE id_hoteles = %s;"""

        self.bd.statement(sql_update, (nombre, direccion_hotel, ciudad, id))
        return {"statusCode": 204, "data": data}

    def _select_hotel_by_id(self, id: int) -> bool:
        sql_select = f"""SELECT id_hoteles FROM tbl_hoteles WHERE id_hoteles = {id} and activo = 1"""
        hotels = self.bd.select(sql_select)
        return False if len(hotels) == 0 else True
