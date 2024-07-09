from fastapi import APIRouter, Depends, HTTPException, status
from models.developers import Developers
from models.companies import Company
from config.database import get_database
from bson import ObjectId
from utils.jwt import create_access_token, verify_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

db = get_database()
dev_collection = db['dev_collection']
company_collection = db['company_collection']

@router.post('/register/developer', response_model=Developers)
async def register_developer(dev: Developers):
    dev.hash_password()
    dev_dict = dev.model_dump()
    result = await dev_collection.insert_one(dev_dict)
    new_dev = await dev_collection.find_one({"_id": result.inserted_id})
    if new_dev is None:
        raise HTTPException(status_code=404, detail="Developer not found after creation")
    return Developers(**new_dev)

@router.post('/register/company', response_model=Company)
async def register_company(company: Company):
    company.hash_password()
    company_dict = company.model_dump()
    result = await company_collection.insert_one(company_dict)
    new_company = await company_collection.find_one({"_id": result.inserted_id})
    if new_company is None:
        raise HTTPException(status_code=404, detail="Company not found after creation")
    return Company(**new_company)

@router.post('/login/developer')
async def login_developer(form_data: OAuth2PasswordRequestForm = Depends()):
    dev = await dev_collection.find_one({"email": form_data.username})
    if dev and Developers(**dev).verify_password(form_data.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": dev["email"]}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post('/login/company')
async def login_company(form_data: OAuth2PasswordRequestForm = Depends()):
    company = await company_collection.find_one({"email": form_data.username})
    if company and Company(**company).verify_password(form_data.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": company["email"]}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get('/users/me')
async def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"email": payload.get("sub")}
