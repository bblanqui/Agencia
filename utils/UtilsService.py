from typing import Dict, List, Union, Any, Callable


def exclude_fields(hotels: list) -> list:
    # Convertir valores bytes a cadenas en todos los hoteles
    for hotel in hotels:
        for key, value in hotel.items():
            if isinstance(value, bytes):
                hotel[key] = value.decode('utf-8')

    return hotels


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            return {"statusCode": 500, "error": str(e)}

    return wrapper


def validate_required_fields(data: Dict[str, Union[None, int, str]], valid: str) -> None:
    if valid == "update":
        required_fields = ["id", "nombre_hotel", "direccion_hotel", "ciudad"]
    elif valid == "login":
        required_fields = ["usuario", "password"]
    else:
        required_fields = ["nombre_hotel", "direccion_hotel", "ciudad"]

    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValueError(f"El campo '{field}' es obligatorio y no puede ser nulo.")


def validate_required_fields_habitacion(data: Dict[str, Union[None, int, str]], valid: str) -> None:
    if valid == "update":
        required_fields = ["id_habitacion", "id_hotel", "costo_habitacion", "ubicacion", "impuesto", "tipo"]
    elif valid == "login":
        required_fields = ["usuario", "password"]
    else:
        required_fields = ["id_hotel", "costo_habitacion", "ubicacion", "impuesto", "tipo"]

    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValueError(f"El campo '{field}' es obligatorio y no puede ser nulo.")


def validate_required_fields_search(data: Dict[str, Union[None, int, str]]) -> None:
    required_fields = ["fecha_entrada", "fecha_salida", "cantidad_persona", "ciudad"]

    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValueError(f"El campo '{field}' es obligatorio y no puede ser nulo.")


def validate_required_fields_reserva(data: Dict[str, Union[None, int, str]]) -> None:
    required_fields = ["id_habitacion", "fecha_entrada",
                       "fecha_salida", "cantidad_persona",
                       "correo_cliente", "telefono_cliente",
                       "nombre_contacto_emergencia",
                       "telefono_contacto_emergencia",
                       "telefono_contacto_emergencia",
                       "nombre_cliente",
                       "genero",
                       "tipo_documento",
                       "numero_documento",
                       "fecha_nacimiento"

                       ]

    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValueError(f"El campo '{field}' es obligatorio y no puede ser nulo.")


from datetime import datetime


def format_date_string(date_str):
    if isinstance(date_str, str):
        try:
            date = datetime.fromisoformat(date_str)
            return date.strftime("%Y-%m-%d %H:%M:%S")  # Formato deseado para las fechas
        except ValueError:
            return date_str  # Si no se puede parsear, devolvemos la cadena original
    else:
        return str(date_str)


def exclude_fields2(hotels: list) -> list:
    # Convertir valores bytes a cadenas en todos los hoteles
    for hotel in hotels:
        for key, value in hotel.items():
            if isinstance(value, bytes):
                hotel[key] = value.decode('utf-8')

        # Formatear las fechas dentro del hotel
        if 'fecha_entrada' in hotel:
            hotel['fecha_entrada'] = format_date_string(hotel['fecha_entrada'])
        if 'fecha_salida' in hotel:
            hotel['fecha_salida'] = format_date_string(hotel['fecha_salida'])
        if 'fecha_reserva' in hotel:
            hotel['fecha_reserva'] = format_date_string(hotel['fecha_reserva'])
        if 'fecha_nacimiento' in hotel:
            hotel['fecha_nacimiento'] = format_date_string(hotel['fecha_nacimiento'])

    return hotels
