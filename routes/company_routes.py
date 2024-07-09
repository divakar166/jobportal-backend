from fastapi import APIRouter, HTTPException, status, Depends
from models.companies import Company
from config.database import get_database
from schemas.companies import company_list_serial
from bson import ObjectId
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection

router = APIRouter()

# Dependency to get the database collection
def get_company_collection(db=Depends(get_database)) -> AsyncIOMotorCollection:
    return db['company_collection']

@router.get('/', response_model=List[Company])
async def get_companies(company_collection: AsyncIOMotorCollection = Depends(get_company_collection)):
    companies = await company_collection.find().to_list(length=None)
    return company_list_serial(companies)

@router.post('/', response_model=Company)
async def post_company(company: Company, company_collection: AsyncIOMotorCollection = Depends(get_company_collection)) -> Company:
    company_dict = company.model_dump()
    result = await company_collection.insert_one(company_dict)
    new_company = await company_collection.find_one({"_id": result.inserted_id})
    if new_company is None:
        raise HTTPException(status_code=404, detail="Company not found after creation")
    return Company(**new_company)

@router.put("/{id}", response_model=Company)
async def put_company(id: str, company: Company, company_collection: AsyncIOMotorCollection = Depends(get_company_collection)):
    update_result = await company_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": company.model_dump()},
        return_document=True
    )
    if update_result is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return update_result

@router.delete("/{id}", response_model=dict)
async def delete_company(id: str, company_collection: AsyncIOMotorCollection = Depends(get_company_collection)):
    delete_result = await company_collection.find_one_and_delete({"_id": ObjectId(id)})
    if delete_result is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Successfully deleted"}
