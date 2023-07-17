from external_api.router import router
from fastapi import FastAPI

from src_ext.external_api import config

app = FastAPI(debug=config.DEBUG, name=config.API_NAME)

app.include_router(router, tags=['ExternalAPI'])
