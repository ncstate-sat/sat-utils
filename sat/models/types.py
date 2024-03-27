from pydantic import AfterValidator
from typing_extensions import Annotated


def validate_campus_id(value):
    try:
        int(value)
    except ValueError:
        raise ValueError("Campus ID must be a parsable number")
    if len(str(value)) != 9:
        raise ValueError("Campus ID must be 9 characters long")


CAMPUS_ID = Annotated[str, AfterValidator(validate_campus_id)]
