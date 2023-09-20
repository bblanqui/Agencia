from typing import Dict

from database.DataBase import Database
import json

from utils.GenerateToken import generate_jwt_token
from utils.UtilsService import exclude_fields, handle_exceptions, validate_required_fields


class ServicioUser:
    def __init__(self):
        self.bd = Database()

    def select_user_by_id(self, id_user: str, ruta: str) -> list:
        sql_select = f"""select ruta  from tbl_users inner join tbl_rutas_user tru on tbl_users.id_users  = tru.usuario 
                        inner join tbl_rutas tr on tr.id_ruta = tru.id_rutas where tbl_users.usuario  = {id_user} and ruta = '{ruta}'"""
        ruta_user = self.bd.select(sql_select)
        return ruta_user

    @handle_exceptions
    def login_user(self, event: dict) -> dict:
        data = json.loads(event['body'])
        validate_required_fields(data, "login")
        usuario = data["usuario"]
        password = data["password"]
        sql_select = f"""select usuario  from tbl_users where usuario = '{usuario}' and password = '{password}'"""
        user = self.bd.select(sql_select)
        if len(user) == 0:
            return {"statusCode": 401, "data": "user o password  incorrect"}
        token = generate_jwt_token(usuario)
        return {"statusCode": 200, "token": token}
