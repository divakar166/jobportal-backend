from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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

@app.get("/", response_class=HTMLResponse)
def index():
    html_content = """
    <html>
        <head>
            <title>Connect - JobPortal Backend</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
                *{
                    font-family:"Inter";
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center; margin-top: 20%;color:#a855f7;font-weight:900;">Welcome to Connect - JobPortal Backend</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
