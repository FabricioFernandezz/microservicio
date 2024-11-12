import unittest
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os

load_dotenv()

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        conn_params = {
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "sslmode": os.getenv("DB_SSLMODE"),
        }

        try:
            connection = psycopg2.connect(**conn_params)
            print("Conexión exitosa a la base de datos")  
            connection.close()  
            self.assertTrue(True)
        except OperationalError as e:
            self.fail(f"Fallo de conexión a la base de datos: {e}")

if __name__ == "__main__":
    unittest.main()
