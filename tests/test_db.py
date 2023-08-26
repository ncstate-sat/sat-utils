from unittest import main, mock, TestCase
from unittest.mock import patch, Mock
from sat.db import get_db_connection, ConnectionType as ctype, pyodbc
from pyodbc import InterfaceError

class TestDatabaseConnectivity(TestCase):

    def test_get_db_connection_pyodbc_bad_connection_string(self):
        conn_string = "Bad Connection String"
        with self.assertRaises(Exception) as _:
            get_db_connection(conn_string, ctype.SQL)

    def test_get_db_connection_cx_Oracle_bad_connection_string(self):
        conn_string = "Bad Connection String"
        with self.assertRaises(Exception) as _:
            get_db_connection(conn_string, ctype.ORACLE)
