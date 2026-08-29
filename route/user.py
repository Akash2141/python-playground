from fastapi import APIRouter, Response, HTTPException, status
from pydantic import BaseModel
from log import toLog

user_router=APIRouter(tags=["USERS"])
USERS=[]
user_id=1

class UserBase(BaseModel):
    name:str
    age:int

class UserCreate(UserBase):
    password:str
    pass

class UserUpdate(UserBase):
    id:int

class UserResponse(BaseModel):
    id:int
    name:str
    age:int

class User(BaseModel):
    id:int
    name:str
    age:int

@user_router.get("/",response_model=list[UserResponse])
@toLog("Hello get Users")
async def get_users() -> list[UserResponse]:
    return USERS

@user_router.post("/create")
@toLog("Hello Create Users")
async def create_users(user_create:UserCreate) -> UserResponse:
    global user_id
    user = User(id=user_id, name=user_create.name, age=user_create.age)
    USERS.append(user)
    user_id+=1
    return UserResponse(**user.model_dump())

@user_router.get("/{id}")
async def get_user(id:int):
    return next((user for user in USERS if user.id==id), HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found"))
    
