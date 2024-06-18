from fastapi import FastAPI, Depends, HTTPException,APIRouter
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth import models, schemas
from src.database import get_async_sessioon, engine
from src.auth.schemas import UserResponse

user_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def transform_pwd(password:str) -> str:
    return pwd_context.hash(password)


@user_router.post("/", response_model=UserResponse)
async def  create_new_user(user: schemas.UserCreate, 
                    db: AsyncSession = Depends(get_async_sessioon)):
    result = result = await db.execute(select(models.User).filter(models.User.login == user.login))
    db_user = result.scalars().first()
    if db_user:
        raise HTTPException(status_code=400, detail="I've alredy seen this login, please try another")
    new_user = models.User(
        fullname = user.fullname,
        login = user.login,
        hashed_password = transform_pwd(user.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    user_response = UserResponse.from_orm(new_user)
    return user_response
