from fastapi import APIRouter, HTTPException, status, Depends
from models.jobs import Job
from config.database import get_database
from schemas.jobs import job_list_serial
from bson import ObjectId
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import BaseModel

router = APIRouter()

# Dependency to get the database collection
def get_job_collection(db=Depends(get_database)) -> AsyncIOMotorCollection:
    return db['job_collection']

class JobUpdate(BaseModel):
    title: str
    description: str
    salary: float
    location: str
    company: str

@router.get('/', response_model=List[Job])
async def get_jobs(job_collection: AsyncIOMotorCollection = Depends(get_job_collection)):
    jobs = await job_collection.find().to_list(length=None)
    return job_list_serial(jobs)

@router.post('/', response_model=Job)
async def post_jobs(job: Job, job_collection: AsyncIOMotorCollection = Depends(get_job_collection)) -> Job:
    job_dict = job.model_dump()
    result = await job_collection.insert_one(job_dict)
    new_job = await job_collection.find_one({"_id": result.inserted_id})
    if new_job is None:
        raise HTTPException(status_code=404, detail="Job not found after creation")
    return Job(**new_job)

@router.put("/{id}", response_model=Job)
async def put_jobs(id: str, job: JobUpdate, job_collection: AsyncIOMotorCollection = Depends(get_job_collection)):
    update_result = await job_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": job.model_dump()},
        return_document=True
    )
    if update_result is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return update_result

@router.delete("/{id}", response_model=dict)
async def delete_jobs(id: str, job_collection: AsyncIOMotorCollection = Depends(get_job_collection)):
    delete_result = await job_collection.find_one_and_delete({"_id": ObjectId(id)})
    if delete_result is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Successfully deleted"}
