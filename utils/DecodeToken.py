import json
import jwt
from os import environ
from functools import wraps
from servicio.ServicioUser import ServicioUser

SECRET_KEY = environ.get('KEY_TOKEN')

user_service = ServicioUser()


def require_token(func):
    @wraps(func)
    def wrapper(event, context):
        global payload
        token1 = event.get('headers', {}).get('Authorization')
        ruta = event.get("path")
        if not token1:
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "No autorizado"})
            }
        if not token1.startswith("Bearer "):
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "Formato de token no válido"})
            }
        token = token1.split(" ")[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_route = user_service.select_user_by_id(payload["user_id"], ruta)

        except jwt.ExpiredSignatureError:
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "Token de autorización expirado"})
            }
        except jwt.DecodeError:
            return {

                "statusCode": 401,
                "body": json.dumps({"message": "Invalid Token"})
            }
        if len(user_route) == 0:
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "No autorizado"})
            }

        return func(event, context)

    return wrapper
