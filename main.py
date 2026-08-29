from fastapi import FastAPI
from route.user import user_router
from settings import settings

print(f"Settings {settings.test}")
app = FastAPI()

app.include_router(user_router, prefix="/user")