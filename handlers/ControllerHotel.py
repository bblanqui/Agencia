from servicio.ServicioHotel import ServicioHotel
import json

hotel_servicio = ServicioHotel()


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
        "statusCode": 200,
        "body": json.dumps({"Result": result}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    return response
