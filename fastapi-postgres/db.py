import psycopg2

class pg:
    @classmethod
    def connect(cls):
        cls.conn = psycopg2.connect(
            host= "localhost",
            database= "socialnetwork",
            user = "postgres",
            password = "918918918"
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def execute(cls, sql: str):
        cls.connect()
        cls.cursor.execute(sql)
        cls.close()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.conn.close()

