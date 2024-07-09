from bson import ObjectId

def dev_list_serial(dev_list):
    return [dev_serial(dev) for dev in dev_list]

def dev_serial(dev) -> dict:
    return {
        "id": str(dev["_id"]),
        "name": dev["name"],
        "email": dev["email"],
        "mobile": dev["mobile"],
        "designation": dev["designation"]
    }