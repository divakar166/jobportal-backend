from pydantic import BaseModel, EmailStr

class Developers(BaseModel):
    name:str
    email:EmailStr
    passwordHash:str
    mobile:str
    designation:str