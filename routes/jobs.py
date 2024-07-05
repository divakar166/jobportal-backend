from fastapi import APIRouter
from models.jobs import Job
from config.database import job_collection
from schemas.jobs import job_list_serial
from bson import ObjectId

job_router = APIRouter()


@job_router.get('/')
async def get_jobs():
    jobs = job_list_serial(job_collection.find())
    return jobs


@job_router.post('/')
async def post_jobs(job: Job) -> Job:
    job = job_collection.insert_one(dict(job))
    new_job = await job_collection.find_one({"_id": job.inserted_id})
    return Job(**new_job)


@job_router.put("/{id}")
async def put_jobs(id: str, job: Job):
    job_collection.find_one_and_update({"_id": ObjectId(id)},
                                       {"$set": dict(job)})
    job = job_collection.find_one({"_id": ObjectId(id)})
    return {"message": job}


@job_router.delete("/{id}")
async def delete_jobs(id: str):
    job_collection.find_one_and_delete({"_id": ObjectId(id)})
    return "Successful"
