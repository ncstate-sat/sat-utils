# SAT Utilities

This repository contains a collection of shared utility functions.

-   AuthChecker: A class that checks if a user has the specified role in their JWT payload
    ([view usage](https://github.ncsu.edu/SAT/csgold-proxy/blob/059191b16890db2679c93e19883cad4a482741ca/app.py#L36))
-   Slack: A class to upload files to our Slack workspace
-   DB: Manage connections for our databases ([docs](https://github.ncsu.edu/SAT/sat-utils/blob/main/docs/db.md))

## Usage

```bash
# Install the package from private PyPI (CLI)
$ pip install -i https://pypi.ehps.ncsu.edu sat-utils

# Install the package from private PyPI (requirements.txt)
$ pip install -r requirements.txt --extra-index-url https://pypi.ehps.ncsu.edu
```

```bash
# Import a class from sat-utils
>>> from sat_utils.auth_checker import AuthChecker

# Import get db function
>>> from sat_utils.db import get_ccure_db_conn
```
