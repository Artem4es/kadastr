from fastapi import FastAPI

from kadastr.router import router as kad_router
from src.kadastr import config

app = FastAPI(debug=config.DEBUG, name=config.API_NAME)

app.include_router(kad_router, tags=['kadastr'])
