import pyodbc
import cx_Oracle
import mysql.connector


def get_portal_db_conn(cfg):
    return pyodbc.connect(cfg['feed_prod'])


def get_fmi_db_conn(cfg):
    return pyodbc.connect(cfg['fmi_prod'])


def get_ccure_db_conn(cfg):
    return pyodbc.connect(cfg['ccure_prod'])


def get_diester_db_conn(cfg):
    return pyodbc.connect(cfg['deister_prod'])


def get_ps_db_conn(cfg):
    return cx_Oracle.connect(cfg['hrprd'])


def get_gold_db_conn(cfg):
    return cx_Oracle.connect(cfg['gold'])


def get_csprd_db_conn(cfg):
    return cx_Oracle.connect(cfg['csprd'])


def get_sims_db_conn(cfg):
    return pyodbc.connect(cfg['sims_prod'])


def get_genetec_db_conn(cfg):
    return pyodbc.connect(cfg['genetec_prod'])


def get_wos_connection(cfg):
    connection = mysql.connector.connect(**(cfg["wos_prod"]))
    return connection


def get_pci_connection(cfg):
    connection = pyodbc.connect(cfg['pci_prod'])
    return connection
