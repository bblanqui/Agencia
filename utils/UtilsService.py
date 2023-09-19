from typing import Dict, List, Union, Any, Callable


def exclude_fields(hotels: list, *fields) -> list:
    # Convertir valores bytes a cadenas en todos los hoteles
    for hotel in hotels:
        for key, value in hotel.items():
            if isinstance(value, bytes):
                hotel[key] = value.decode('utf-8')

    # Excluir los campos especificados
    excluded_fields = []
    for hotel in hotels:
        exclude = {k: v for k, v in hotel.items() if k not in fields}
        excluded_fields.append(exclude)

    return excluded_fields


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
    else:
        required_fields = ["nombre_hotel", "direccion_hotel", "ciudad"]

    for field in required_fields:
        if field not in data or data[field] is None:
            raise ValueError(f"El campo '{field}' es obligatorio y no puede ser nulo.")
