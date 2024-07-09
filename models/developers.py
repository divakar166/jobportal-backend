from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Developers(BaseModel):
    name: str
    email: EmailStr
    password: str
    mobile: str
    designation: str

    def hash_password(self):
        self.password = pwd_context.hash(self.password)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)