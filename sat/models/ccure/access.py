from pydantic import UUID4, BaseModel


class Clearance(BaseModel):
    object_id: int
    guid: UUID4
    name: str


class Credential(BaseModel):
    card_number: int
    patron_id: int
