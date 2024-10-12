from fastapi import FastAPI
from routes.routes import app
from starlette.requests import Request
from starlette.responses import JSONResponse
apps = FastAPI(debug=True)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        return JSONResponse({"status":500,"message":"Send valid parameters"})

apps.middleware('http')(catch_exceptions_middleware)

apps.include_router(app)
