from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Json


class SDoctor(BaseModel):
    first_name: str
    middle_name: str | None
    last_name: str

    fullName: str
    gender: Literal["М", "Ж"]
    birth: datetime
    image_path: str | None

    medical_institution: str | None
    jobTitle: str | None
    contacts: Json | None
    education: Json | None
    career: Json | None

    model_config = ConfigDict(from_attributes=True)  # type: ignore
