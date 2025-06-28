from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import routes
from backend.api import routes_dev  # <--- ADD THIS LINE

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
app.include_router(routes_dev.router)  # <--- AND THIS LINE
