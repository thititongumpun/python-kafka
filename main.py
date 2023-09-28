from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from config import Settings
from functools import lru_cache
from typing_extensions import Annotated
from service.kafkaService import producer

app = FastAPI()


@app.get("/")
async def root():
    for i in range(1, 10):
      producer.produce('cclab', b'Hello World %d' % i)
    return {"message": Settings().broker}

@app.get('/run')
async def produce():
    for i in range(1, 10):
      producer.produce('cclab', b'Hello World %d' % i)
    return {"message": "done"}

# @app.get("/info")
# async def info(settings: Annotated[Settings, Depends(get_settings)]):
#     return {
#         "app_name": settings.app_name,
#         "admin_email": settings.admin_email,
#         "items_per_user": settings.items_per_user,
#     }

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')
