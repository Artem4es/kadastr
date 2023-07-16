from external_api.router import router
from fastapi import FastAPI

app = FastAPI(debug=False, name='ExternalAPI')

app.include_router(router, tags=['ExternalAPI'])
