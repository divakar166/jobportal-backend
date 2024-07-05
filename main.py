from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.developers import dev_router
from routes.companies import company_router
from routes.jobs import job_router

app = FastAPI()

origins = [
    'http://localhost:5173/', 'https://jobportal-divakar166.vercel.app/'
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(dev_router, prefix='/developers')
app.include_router(job_router, prefix='/jobs')
app.include_router(company_router, prefix='/companies')

@app.get("/")
def index():
    {"message": "Welcome to Connect - JobPortal Backend"}

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app)
