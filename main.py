from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from routes import auth_routes, company_routes, dev_routes, job_routes

app = FastAPI()

origins = [
    'http://localhost:5173/', 'https://jobportal-divakar166.vercel.app/'
]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(company_routes.router, prefix="/companies", tags=["companies"])
app.include_router(dev_routes.router, prefix="/developers", tags=["developers"])
app.include_router(job_routes.router, prefix="/jobs", tags=["jobs"])

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
