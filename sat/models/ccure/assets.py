from typing import Optional

from pydantic import UUID4, BaseModel

from sat.models.ccure.types import ASSET_TYPES


class Asset(BaseModel):
    object_id: int
    name: str
    guid: UUID4
    asset_type: Optional[ASSET_TYPES]
