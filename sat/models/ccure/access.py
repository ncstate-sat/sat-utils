from pydantic import BaseModel


class Clearance(BaseModel):
    object_id: int
    guid: str
    name: str


class Credential(BaseModel):
    card_number: int
    patron_id: int
