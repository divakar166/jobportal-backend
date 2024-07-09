from fastapi import APIRouter, HTTPException
from models.developers import Developers
from config.database import get_database
from schemas.devlopers import dev_list_serial
from bson import ObjectId

router = APIRouter()
db = get_database()
dev_collection = db['dev_collection']

@router.get('/')
async def get_devs():
    devs = dev_collection.find()
    dev_list = dev_list_serial(devs)
    print(dev_list)
    return dev_list

@router.post('/')
async def post_devs(dev: Developers) -> Developers:
    dev.hash_password()
    dev_dict = dev.model_dump()
    result = await dev_collection.insert_one(dev_dict)
    new_dev = await dev_collection.find_one({"_id": result.inserted_id})
    if new_dev is None:
        raise HTTPException(status_code=404, detail="Developer not found after creation")
    return Developers(**new_dev)

@router.put("/{id}")
async def put_devs(id: str, dev: Developers):
    dev_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(dev)})
    updated_dev = await dev_collection.find_one({"_id": ObjectId(id)})
    return {"message": updated_dev}

@router.delete("/{id}")
async def delete_devs(id: str):
    dev_collection.find_one_and_delete({"_id": ObjectId(id)})
    return "Successful"
