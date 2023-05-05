# SAT Utilities

This repository contains a collection of shared utility functions.

- Slack: A class to upload files to our Slack workspace
- SATLogger: A standard logger for SAT projects

## Installation

```shell
# Install the package from private PyPI (CLI)
$ pip install -i https://pypi.ehps.ncsu.edu sat-utils

# Install the package from private PyPI (requirements.txt)
$ pip install -r requirements.txt --extra-index-url https://pypi.ehps.ncsu.edu
```

## Usage

### Slack

```python
from sat.slack import Slack

message = Slack(token="abc123-8dkhnna-97hasdj-xyz")
message.upload_file(channel="support", file_path="C:/files", file_name="support.pdf", file_type="", title="Support manual v3.2", initial_comment="Woot!")
```

### SATLogger

```python
from sat.logs import SATLogger
logger = SATLogger(__name__)

...
logger.info("Hello, world!")
```
