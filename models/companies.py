from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Company(BaseModel):
    name: str
    email: EmailStr
    password: str
    website: Optional[str] = None
    description: Optional[str] = None
    registration_date: datetime
    job_opportunities_posted: int
    candidates_hired: int

    def hash_password(self):
        self.password = pwd_context.hash(self.password)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)