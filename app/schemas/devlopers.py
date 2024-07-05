def dev_serial(developer) -> dict:
    return {
        "id":str(developer["_id"]),
        "name":developer["name"],
        "email":developer['email'],
        "mobile":developer['mobile'],
        "designation":developer['designation']
    }

def dev_list_serial(developers) -> list:
    return [dev_serial(developer) for developer in developers]