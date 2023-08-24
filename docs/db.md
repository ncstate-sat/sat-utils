# Database Module

The dabase module aims to standardize how we connect to our data environments

It currently supports two database engines, Oracle and SQL server. 
Support for SQL server is provided by pyodbc while support for Oracle is provided by cx_Oracle.

There are two methods implemented by the module. The first method takes a 
connection string paramater and an engine paramater and connects to the
appropriate db engine.

The second is a helper method that takes an envornment variable name 
and retrieves the connection string from the environment and calls the primary.

Lastly, there is an Enum that explicitly defines the types.
The current values are ConnectionType.SQL and ConnectionType.ORACLE.

__install__

`pip install --extra-index https://pypi.ehps.ncsu.edu sat-utils`

__getting connected with a connection string__

```
from sat.db import get_db_connection
from os import getenv

connection_string = 'user/password@localhost/orcl'
connection = get_db_connection(connection_string, ctype.ORACLE)
```

__getting connected with an environment variable__

```
from sat.db import ConnectionType as ctype, get_named_db_connection

connection = get_db_connection('ENV_PROD_CONNECTION', ctype.ORACLE)
```