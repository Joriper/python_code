from fastapi import FastAPI
from routes.routes import app

apps = FastAPI(debug=True)

apps.include_router(app)