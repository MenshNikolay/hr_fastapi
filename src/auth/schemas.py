from pydantic import BaseModel, EmailStr, Field, constr
from enum import Enum
from typing import Optional

class RoleEnum(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"


class UserCreate(BaseModel):
    id: int
    name: str = constr(min_length=3, max_length=20)
    surname: str = constr(min_length=2, max_length=20)
    email: EmailStr
    pasword: str = constr(min_length=6)
    role: RoleEnum = RoleEnum.viewer

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[constr(min_length=3, max_length=20)] = None
    surname: Optional[constr(min_length=2, max_length=20)] = None
    password: Optional[constr(min_length=8)] = None
    role: Optional[RoleEnum] = None

class UserResponse(BaseModel):
    id: int
    name: str 
    surname: str 
    email: EmailStr
    role: RoleEnum 

    class Config:
        ORM = True