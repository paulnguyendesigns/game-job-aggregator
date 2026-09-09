from datetime import date
from typing import Optional
from enum import Enum
from pydantic import BaseModel, HttpUrl, computed_field, model_validator

class Category(str, Enum):
    PROGRAMMING = "Programming"
    GAME_DESIGN = "Game Design"
    ART = "Art"
    PRODUCTION = "Production"
    QA = "QA"
    OTHER = "Other"
    

class Job(BaseModel):
    company: str
    role: str
    application_url: HttpUrl
    remote: bool = False
    category: Category
    technologies: list[str] = []

    location: Optional[str] = None
    country: Optional[str] = None
    date_posted: Optional[date] = None

    @computed_field
    @property
    def set_age_days(self) -> Optional[str]:
        if self.date_posted is None:
            return None
        days = (date.today() - self.date_posted).days
        return f"{days}d"

    @model_validator(mode="after")
    def set_location_placeholder(self):
        if self.location is not None:
            return self
        if self.country and self.remote:
            self.location = f"Remote in {self.country}"
        else:
            self.location = "Unknown"
        return self