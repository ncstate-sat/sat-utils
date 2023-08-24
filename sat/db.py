from os import getenv
from sat.logs import SATLogger

import cx_Oracle
import pyodbc

logger = SATLogger(name=__name__)

def _get_connection_string(conn_env_var):
    """
    A helper function that returns a database connection
    string from the environemnt.

    Parameters
    ----------
    conn_env_var: str
        The environment variable that contains the database 
        connection string you are trying to connect to.
    """

    try:
        connection_string = getenv(conn_env_var)
        return connection_string
    except ValueError as _error:
        logger.error("There was an error retrieveing the connection string. Does {conn_env_var} exist in hte local environment?")
        logger.error(_error)

def get_db_connection(conn_string:str, type:str):
    """
    A function that returns a database connection.

    Parameters
    ----------
    conn_str: str
        The database specific connection string you are opening 
         a connection to.
    type: str
        The database drive the connection uses.
        Currently only 'oracle' or 'sql' are supported options.
    return: Returns a database connection object
    """
    accepted_drivers = ['oracle', 'sql']

    if type.lower() not in accepted_drivers:
        raise ValueError("Invalid driver type option: {type}")
    try:
        if type.lower() == 'sql': 
            return pyodbc.connect(conn_string)
        
        return cx_Oracle.connect(conn_string)
    except Exception as error:
        logger.error("There was an error connecting to the database\n {error}")

def get_named_db_connection(db_env_name:str, type:str):
    """
    A function that returns a database connection.

    Parameters
    ----------
    db_env_name: str
        The name of a defined environment variable that contains a 
         specific connection string you are opening a connection to.
    type: str
        The database drive the connection uses.
        Currently only 'oracle' or 'sql' are supported options.
    return: Returns a database connection object 
    """
    _conn_string = _get_connection_string(db_env_name)
    return get_db_connection(conn_string=_conn_string, type=type)
    