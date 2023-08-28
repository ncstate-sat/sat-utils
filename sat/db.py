from enum import Enum

import cx_Oracle
import pyodbc


class SatDBException(BaseException):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


class ConnectionType(Enum):
    ORACLE = 1
    SQL = 2


def get_db_connection(conn_string: str, type: ConnectionType):
    """
    A function that returns a database connection.

    Parameters
    ----------
    conn_str: str
        The database specific connection string you are opening
         a connection to.
    type: ConnectionType
        The database driver the connection uses.
    return: Returns a database connection object
    """
    try:
        if type == ConnectionType.SQL:
            return pyodbc.connect(conn_string)
        return cx_Oracle.connect(conn_string)
    except Exception as error:
        raise SatDBException(
            f"There was an {error.__class__.__name__} when connecting to the database.", error
        )
