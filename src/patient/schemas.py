from datetime import datetime

from pydantic import BaseModel, ConfigDict, Json


class SPatient(BaseModel):
    gender: str
    birth: datetime

    status: str | None
    discussion: int | None
    comment: str | None
    visits: Json | None
    body_info: Json | None

    laboratoryTests: Json | None
    instrumentalStudies: Json | None
    surgicalTreatment: Json | None

    model_config = ConfigDict(from_attributes=True)  # type: ignore
