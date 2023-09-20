import jwt
import datetime
from os import environ

# Clave secreta para firmar el token (debe ser la misma que se utiliza para verificarlo)
SECRET_KEY = environ.get('KEY_TOKEN')


def generate_jwt_token(user_id: str) -> str:
    # Definir los datos del token
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Tiempo de expiración del token
    }

    # Generar el token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token
