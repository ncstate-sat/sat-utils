from typing import Optional

from pydantic import BaseModel


class Asset(BaseModel):
    object_id: int
    name: str
    guid: str
    type: str


class Door(BaseModel):
    object_id: int
    name: str
    guid: str
    description: Optional[str] = ""


class Elevator(BaseModel):
    object_id: int
    name: str
    guid: str
    description: Optional[str] = ""
