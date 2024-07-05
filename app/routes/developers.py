from fastapi import APIRouter
from models.developers import Developers
from config.database import dev_collection
from schemas.devlopers import dev_list_serial
from bson import ObjectId

dev_router = APIRouter()


@dev_router.get('/')
async def get_devs():
    devs = dev_list_serial(dev_collection.find())
    return devs


@dev_router.post('/')
async def post_devs(dev: Developers) -> Developers:
    dev = dev_collection.insert_one(dict(dev))
    new_dev = await dev_collection.find_one({"_id": dev.inserted_id})
    return Developers(**new_dev)


@dev_router.put("/{id}")
async def put_devs(id: str, dev: Developers):
    dev_collection.find_one_and_update({"_id": ObjectId(id)},
                                       {"$set": dict(dev)})
    dev = dev_collection.find_one({"_id": ObjectId(id)})
    return {"message": dev}


@dev_router.delete("/{id}")
async def delete_devs(id: str):
    dev_collection.find_one_and_delete({"_id": ObjectId(id)})
    return "Successful"
