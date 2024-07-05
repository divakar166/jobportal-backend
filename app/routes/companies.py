from fastapi import APIRouter
from models.companies import Company
from config.database import company_collection
from schemas.companies import company_list_serial
from bson import ObjectId

company_router = APIRouter()


@company_router.get('/')
async def get_companies():
    companies = company_list_serial(company_collection.find())
    return companies


@company_router.post('/')
async def post_company(company: Company) -> Company:
    company = company_collection.insert_one(dict(company))
    new_company = company_collection.find_one({"_id": company.inserted_id})
    return Company(**new_company)


@company_router.put("/{id}")
async def put_company(id: str, company: Company):
    company_collection.find_one_and_update({"_id": ObjectId(id)},
                                           {"$set": dict(company)})
    updatedCompany = company_collection.find_one({"_id": ObjectId(id)})
    return {"message": updatedCompany}


@company_router.delete("/{id}")
async def delete_company(id: str):
    company_collection.find_one_and_delete({"_id": ObjectId(id)})
    return "Successful"
