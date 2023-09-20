from servicio.ServicioHotel import ServicioHotel
import json
from utils.DecodeToken import require_token
from servicio.ServicioUser import ServicioUser
from servicio.ServicioHabitacion import ServicioHabitacion
from servicio.ServicioSearchHotel import ServicioSearchHotel
from servicio.ServicioReservaHotel import ServicioReservaHotel


hotel_servicio = ServicioHotel()
user_service = ServicioUser()
habitacion_services = ServicioHabitacion()
search_hotel_date = ServicioSearchHotel()
reserva_hotel_cliente = ServicioReservaHotel()

@require_token
def hotel_service(event, context):
    global result
    method = event['httpMethod']
    parametros_url = event['queryStringParameters']
    if method == "GET" and parametros_url is None:
        result = hotel_servicio.select_hotel()
    elif method == "GET" and parametros_url is not None:
        result = hotel_servicio.deactivate_hotel(int(parametros_url['id']))
    elif method == "POST":
        result = hotel_servicio.insert_hotel(event)
    elif method == "PUT":
        result = hotel_servicio.update_hotel(event)
    response = {
        "statusCode": result["statusCode"],
        "body": json.dumps({"Result": result})
    }
    return response


def login(event, context):
    result = user_service.login_user(event)
    response = {
        "statusCode": result["statusCode"],
        "body": json.dumps({"Result": result})
    }
    return response


@require_token
def habitacion_service(event, context):

    global result
    method = event['httpMethod']
    parametros_url = event['queryStringParameters']
    if method == "GET" and parametros_url is None:
        result = habitacion_services.select_habitacion()
    elif method == "GET" and parametros_url is not None:
        result = habitacion_services.deactivate_habitacion(int(parametros_url['id']))
    elif method == "POST":
        result = habitacion_services.insert_habitacion(event)
    elif method == "PUT":
        result = habitacion_services.update_habitacion(event)
    response = {
        "statusCode": result["statusCode"],
        "body": json.dumps({"Result": result})
    }
    return response


def search_hotel(event, context):

    result = search_hotel_date.seach_hotel(event)
    response = {
        "statusCode": result["statusCode"],
        "body": json.dumps({"Result": result})
    }
    return response


def reserva_hotel(event, context):

    result = reserva_hotel_cliente.insert_reserva(event)
    response = {
        "statusCode": result["statusCode"],
        "body": json.dumps({"Result": result})
    }
    return response
