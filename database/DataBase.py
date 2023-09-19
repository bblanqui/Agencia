import pymysql
from os import environ


class Database:

    def __init__(self):
        self.host = environ.get('DB_HOST')
        self.user = environ.get('DB_USER')
        self.password = environ.get('DB_PASSWORD')
        self.db = environ.get('DB_NAME')

    def conexion(self):

        connection = pymysql.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    def select(self, sql):
        connection = self.conexion()
        result = False
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

        finally:

            connection.close()

        return result

    def statement(self, sql, values=None):
        connection = self.conexion()
        result = False
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
                result = cursor.lastrowid
            connection.commit()
        finally:
            connection.close()

        return result
