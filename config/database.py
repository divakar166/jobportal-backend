from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# client = MongoClient(os.environ.get('MONGODB_URI'))
# db = client.job_portal

# dev_collection = db["developers"]
# company_collection = db["companies"]
# job_collection = db["jobs"]

DATABASE_URL = os.environ.get("MONGODB_URI")

client = AsyncIOMotorClient(DATABASE_URL)
database = client['job_portal']

def get_database():
    return database