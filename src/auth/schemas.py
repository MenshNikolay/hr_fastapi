from pydantic import BaseModel, EmailStr, Field, constr
from enum import Enum
from typing import Optional
from datetime import date

class SatusEnum(str, Enum):
    unprocessing = "Не в работе"
    processing = "В работе"
    denied = "Отказ"
    closed = "Сделка закрыта"


class ClientCreate(BaseModel):
    account_number: str = constr(min_length=20, max_length=20)
    name: str 
    surname: str 
    father_name: str
    b_day: date
    inn: int = constr(min_length=12, max_length=12)
    supervisor: str
    status: SatusEnum = SatusEnum.unprocessing


class UserCreate(BaseModel):
    fullname:str 
    login:str
    password:str   
    

class ClientResponse(BaseModel):
    
    name: str 
    surname: str 
    father_name: str
    b_day: date
    inn: int
    supervisor: str
    status: SatusEnum

    class Config:
        ORM = True
        from_attributes = True 

class UserResponse(BaseModel):
    
    fullname:str 
    login:str

    class Config:
        ORM = True
        from_attributes = True 
             