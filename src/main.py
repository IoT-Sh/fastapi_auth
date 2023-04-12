from fastapi import FastAPI
from .routs import rout, auth

app = FastAPI()


v1 = FastAPI()
v1.include_router(auth.api)
v1.include_router(rout.api)

app.mount("/api/v1", v1)
