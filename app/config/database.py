from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get('MONGODB_URI'))
db = client.job_portal

dev_collection = db["developers"]
company_collection = db["companies"]
job_collection = db["jobs"]