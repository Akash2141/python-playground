from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()
class MySettings(BaseSettings):
    test:int=1

settings = MySettings()