from fastapi import FastAPI

from kadastr.router import router as kad_router

app = FastAPI()

app.include_router(kad_router, tags=['kadastr'])
