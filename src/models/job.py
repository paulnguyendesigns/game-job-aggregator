from datetime import date
from typing import Optional
from pydantic import BaseModel, HttpUrl, computed_field


class Job(BaseModel):
    company: str
    role: str
    application_url: HttpUrl

    location: Optional[str] = None
    date_posted: Optional[date] = None

    @computed_field
    @property
    def age_days(self) -> Optional[str]:
        if self.date_posted is None:
            return None
        days = (date.today() - self.date_posted).days
        return f"{days}d"