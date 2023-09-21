# Proyecto de Administración de Alojamiento en Hoteles Locales

Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar una plataforma de administración de alojamiento en hoteles locales. La plataforma estará compuesta por varias historias de usuario que permitirán a los agentes de viajes gestionar hoteles y a los viajeros realizar reservas de habitaciones en estos hoteles.

# Requisitos para la Entrega
La aplicación debe ser entregada, desplegada y usable.
Se debe entregar el código fuente por medio del repositorio de su preferencia.

Podrá usar cualquier motor de bases de datos para el almacenamiento.

# Historias de Usuario
# Historia de Usuario 1

Administración de Alojamiento

Descripción

Yo como agencia de viajes deseo crear un hotel en mi lista de hoteles preferidos, con el fin de obtener una comisión más alta.

Criterios de Aceptación

Dado que yo como agente de viajes inicie sesión en mi plataforma de viajes y desee gestionar un hotel, entonces:

El sistema deberá permitir crear un nuevo hotel.

El sistema deberá permitir asignar a cada hotel todas las habitaciones disponibles para reserva.

El sistema deberá permitir modificar los valores de cada habitación.

El sistema deberá permitir modificar los valores de cada hotel.

El sistema me deberá permitir habilitar o deshabilitar cada uno de los hoteles.

El sistema me deberá permitir habilitar o deshabilitar cada una de las habitaciones del hotel.

Dado que yo como agente de viajes inicie sesión en mi plataforma de viajes y desee ver las reservas de hoteles, entonces:

El sistema deberá listar cada una de las reservas realizadas en mis hoteles.

El sistema deberá permitir ver el detalle de cada una de las reservas realizadas.

# Observaciones
Cada habitación deberá permitir registrar el costo base, impuestos y tipo de habitación.

Cada habitación deberá permitir registrar la ubicación en que se encuentra.

# Historia de Usuario 2: 
Reserva de Hoteles

Descripción

Yo como viajero deseo reservar un hotel en la plataforma de viajes de mi preferencia, con el fin de obtener un alojamiento.

Criterios de Aceptación

Dado que yo, como viajero, esté en el buscador de hoteles, entonces:

El sistema me deberá dar la opción de buscar por: fecha de entrada al alojamiento, fecha de salida del alojamiento, cantidad de personas que se alojarán y ciudad de destino.

El sistema me deberá permitir elegir una habitación del hotel de mi preferencia.

El sistema me deberá desplegar un formulario de reserva para ingresar los datos de los huéspedes.

El sistema deberá permitir realizar la reserva de la habitación.
El sistema me deberá notificar la reserva por medio de correo electrónico.

# Observaciones

Los datos de cada pasajero deben ser:

Nombres y apellidos 

Fecha de nacimiento

Género

Tipo de documento

Número de documento

Email

Teléfono de contacto

La reserva deberá asociar un contacto de emergencia, el cual debe contener:

Nombres completos

Teléfono de contacto.



# Tablas Maestras

Tabla de Tipo de Habitación

id_tipo_habitacion    	descripcion
    
    1	            amoblada
    2	            sin amoblar
    3	            con ducha

Tabla de Género

 id_genero  	descripcion

      1	        Masculino
      2	        Femenino

Tabla de Tipo de Documento

id_tbl_tipo_documento	descripcion

        1	      Cedula
        2	     Tarjeta de Identidad


# Tecnología Utilizada
    Plataforma: AWS
    Lenguaje de Programación: Python
    Servicios Serverless
    Base de Datos: RDS con MySQL
    Seguridad: JWT Token para proteger las rutas
# Endpoints
1. Login
Método: POST

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/login

Descripción: Esta ruta permite la autenticación de usuarios administradores.

Cuerpo JSON:

json

    {
      "usuario": "1028029531",
    
      "password": "brian312"
    }


ejemplo de respuesta:

    {
        "Result": {
            "statusCode": 200,
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTAyODAyOTUzMSIsImV4cCI6MTY5NTMwNDcwOH0.dIobCEbsExT_5Xj9ZM0bW-q9x9Hg8pnJ-Fv84HMIJqI"
        }
    }


2. Obtener Hoteles

Método: GET

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HotelService

Descripción: Esta ruta permite obtener la lista de hoteles disponibles.
Requisitos: Ruta protegida por medio de JWT.

ejemplo de respuesta:

    {
        "Result": {
            "statusCode": 200,
            "data": [
                {
                    "id_hoteles": 15,
                    "nombre_hotel": "Moda estren",
                    "direccion_hotel": "Kr 32",
                    "ciudad": "barranquilla"
                }

    }

3. Desactivar Hotel

Método: GET

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HotelService

Descripción: Esta ruta permite desactivar un hotel por su ID.

Parámetros: Se debe proporcionar un "id" para el hotel a desactivar.

Requisitos: Ruta protegida por medio de JWT.

response: status 204 si es correcto o 401 si es incorrecto.


4. Ingresar un Nuevo Hotel

Método: POST

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HotelService

Descripción: Esta ruta permite ingresar un nuevo hotel.

Cuerpo JSON:

json

    {
        "nombre_hotel":"Castilla de oro",
        "direccion_hotel":"kr",
        "ciudad":"Bogota"

    }

response: status 201 si es correcto o 500 si es incorrecto.

5. Actualizar un Hotel

Método: PUT

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HotelService

Descripción: Esta ruta permite actualizar un hotel por su ID.

Cuerpo JSON:

json

    {
        "id": 27,
        "nombre_hotel": "Castilla de oro",
        "direccion_hotel": "direccion",
        "ciudad": "Bogota"
    }

response: status 204 si es correcto o 404 si es incorrecto.

6. Obtener Habitaciones

Método: GET

Endpoint:  https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HabitacionService

Requisitos: Ruta protegida por medio de JWT.

ejemplo de respuesta:

json

    {
        "Result": {
            "statusCode": 200,
            "data": [
                {
                    "id_habitaciones": 7,
                    "id_hotel": 20,
                    "nombre_hotel": "Turbo",
                    "ciudad": "MedellÃ­n",
                    "direccion_hotel": "kr 26 F #38a - 01",
                    "costo": 500000,
                    "ubicacion": "pasillo",
                    "capacidad": 4,
                    "impuesto": 20000.0,
                    "tipo_habitacion": "amoblada",
                    "estado": "No disponible"
                }

    }


7. Ingresar una Nueva Habitación
Método: POST

Endpoint:  https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HabitacionService

Descripción: Esta ruta permite ingresar una nueva habitación en un hotel.

Cuerpo JSON:

    {
        "id_hotel":21,
        "costo_habitacion": 150000,
        "ubicacion":"https://www.google.com/maps/@6.2894904,-75.5711006,3a,75y,288.68h,90t/data=!3m7!1e1!3m5!1sJ-FE-ENPWOZ8Rstqd-i9RQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DJ-FE-ENPWOZ8Rstqd-i9RQ%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D288.68085%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656?entry=ttu",
        "impuesto":35000,
        "tipo":2,
        "capacidad": 3



    }

response: status 201 si es correcto o 404 si es incorrecto.

8. Actualizar una Habitación

Método: PUT

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HabitacionService

Descripción: Esta ruta permite actualizar una habitación en un hotel por su ID.
Cuerpo JSON:
json

    {
        "id_habitacion":11,
        "id_hotel":21,
        "costo_habitacion":21000,
        "ubicacion":"https://www.google.com/maps/@6.2894904,-75.5711006,3a,75y,288.68h,90t/data=!3m7!1e1!3m5!1sJ-FE-ENPWOZ8Rstqd-i9RQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DJ-FE-ENPWOZ8Rstqd-i9RQ%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D288.68085%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656?entry=ttu",
        "impuesto":50000,
        "tipo":2

    }

response: status 204 si es correcto o 404 si es incorrecto.

9. desactivar habitación
Método: GET

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HabitacionService

Descripción: Esta ruta permite desactivar un hotel por su ID.

Parámetros: Se debe proporcionar un "id" para el hotel a desactivar.

Requisitos: Ruta protegida por medio de JWT.




10. Realizar Reserva
Método: POST

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ReservaHotel

Descripción: ESTE ENDPOINT CUMPLE CON VARIOS CRITERIOS

* busca la habitacion y valida que cumpla con los requisitos de la reserva ejemplo la cantidad de personas que se hospedaran ese parametro debe ser igual o menor a la numero basico que hospeda la habitacion

* habitacion y hotel deben estar activas
* busca la habitacion para validar si existe
* busca que no tenga reservas activas por medio de la fecha de entrada y de salida
* inserta en la tabla de detalles de la reserva
* envia el correo al cliente si todas las validaciones se cumplen
* todos los campos son obligatorios
pd: el cuerpo del correo realiza un calculo el cual dice el costo por dia de la habitacion junto con la foto de la habitacion
la ubicacion, el hotel, la direccion y muchas cosas mas.

Cuerpo JSON:

json

    {
            "id_habitacion":12,
            "fecha_entrada":"2024-03-01 14:30:00",
            "fecha_salida":"2024-03-05 14:30:00",
            "cantidad_persona":3,
            "correo_cliente":"acevedomoralescamilo@gmail.com",
            "telefono_cliente":"32054752224",
            "nombre_contacto_emergencia":"Brian Perez",
            "telefono_contacto_emergencia":"32574124441",
            "nombre_cliente":"Camilo Acevedo",
            "genero":1,
            "tipo_documento":1,
            "numero_documento":1028029531,
            "fecha_nacimiento":"2024-03-05 14:30:00"

    }

11. Obtener Reservas

Método: GET

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ObtenerReservas

Descripción: Esta ruta permite obtener la lista de reservas realizadas en los hoteles.

Requisitos: Ruta protegida por medio de JWT.

json 

    {
        "Result": {
            "statusCode": 200,
            "data": [
                {
                    "id_reserva": 36,
                    "id_habitacion": 1,
                    "nombre_reserva": "Luis Gonzales",
                    "numero_documento": "1028029531",
                    "fecha_entrada": "2024-03-01 14:30:00",
                    "fecha_salida": "2024-03-24 14:30:00",
                    "cantidad_persona": 2,
                    "nombre_hotel": "Moda estren",
                    "direccion_hotel": "Kr 32",
                    "ciudad_destino": "barranquilla",
                    "ubicacion": "pasillo",
                    "fecha_reserva": "2023-09-20 16:12:58",
                    "numero_reserva": "59539972-706a-435a-89fa-fc714d5be323",
                    "costo": 500000,
                    "impuesto": 150000.0,
                    "total": 650000.0
                }
    }

12. Obtener Detalle de Reserva
Método: GET

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ObtenerReservaDetalle

Requisitos: Ruta protegida por medio de JWT.

json

  {
      
    "Result": {
        "statusCode": 200,
        "data": [
            {
                "id_detalle_reserva": 1,
                "id_reserva": 38,
                "nombre_cliente": "Luis Gonzales",
                "fecha_nacimiento": "1990-03-01 14:30:00",
                "genero": "1",
                "tipo_documento": "1",
                "email": "correo@example.com",
                "telefono_contacto": "1234567890",
                "numero_reserva": "8c8daf63-dea1-4491-be5d-dfd86c5ae813"
            }

  }

13. Obtener Habitaciones para reserva

Método: POST

Endpoint: https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/SearchHotel

Cuerpo JSON:

json

    {
        "fecha_entrada":"2024-03-01 14:30:00",
        "fecha_salida":"2024-03-01 14:30:00",
        "cantidad_persona":1,
        "ciudad":"bogota"

    }


Descripción: 

este metodo realiza una busqueda por nombre de hotel, fecha de entrada y fecha de salida para obtene una habitacion relacionada con el hotel, las caracteriticas
de las habitaciones como la capacidad de huesped, el estado del hotel debe ser activo y la habitacion debe estar en estado desocupada.
esta ruta devuelve un estado 200 con la data si es correcto, si no devuelve un estado 500 con el error del servidor.

ejemplo de respuesta:

    {
        "Result": {
            "statusCode": 200,
            "data": [
                {
                    "id_hoteles": 27,
                    "nombre_hotel": "Castilla de oro",
                    "direccion_hotel": "direccion_hotel",
                    "ciudad": "Bogota",
                    "id_habitacion": 11,
                    "costo": 21000,
                    "ubicacion": "https://www.google.com/maps/@6.2894904,-75.5711006,3a,75y,288.68h,90t/data=!3m7!1e1!3m5!1sJ-FE-ENPWOZ8Rstqd-i9RQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DJ-FE-ENPWOZ8Rstqd-i9RQ%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D288.68085%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656?entry=ttu",
                    "impuesto": 50000.0,
                    "descripcion": "sin amoblar",
                    "capacidad": 3
                }
            ]
        }


# EndPoints

* ANY - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HotelService
*  POST - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/login
*  ANY - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/HabitacionService
*  POST - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/SearchHotel
*  POST - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ReservaHotel
*  GET - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ObtenerReservas
*  GET - https://6ilqj9erwb.execute-api.us-east-1.amazonaws.com/dev/ObtenerReservaDetalle









