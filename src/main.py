from fastapi import FastAPI

from kadastr.router import router as kad_router

app = FastAPI(debug=False, name='KadastrAPI')

app.include_router(kad_router, tags=['kadastr'])
