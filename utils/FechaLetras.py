def obtener_fecha(fecha_reserva):
    def obtener_nombre_mes(mes):
        nombres_meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        return nombres_meses[mes - 1]

    # Define una función para obtener el nombre del día en español
    def obtener_nombre_dia(dia):
        nombres_dias = [
            "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
        ]
        return nombres_dias[dia]

    # Obtiene el nombre del día y el nombre del mes en español
    nombre_dia = obtener_nombre_dia(fecha_reserva.weekday())
    nombre_mes = obtener_nombre_mes(fecha_reserva.month)

    # Obtiene el día
    dia = fecha_reserva.day

    # Obtiene el año
    ano = fecha_reserva.year

    # Formatea la fecha en el formato deseado
    fecha_en_letras = f"{nombre_dia}, {dia} de {nombre_mes} de {ano}"

    return fecha_en_letras
