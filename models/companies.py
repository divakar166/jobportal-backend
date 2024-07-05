from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from typing import Optional

class Company(BaseModel):
    name: str
    email: EmailStr
    website: Optional[str] = None
    description: Optional[str] = None
    registration_date: datetime
    job_opportunities_posted: int
    candidates_hired: int