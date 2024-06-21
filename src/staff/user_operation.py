from passlib.context import CryptContext
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.database import get_async_sessioon
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import  Depends, HTTPException, status
from sqlalchemy.future import select
from src import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
authentication = HTTPBasic()


def transform_pwd(password:str) -> str:
    return pwd_context.hash(password)



async def get_user(user_credentials: HTTPBasicCredentials = Depends(authentication), 
                   db: AsyncSession = Depends(get_async_sessioon)):
    query = await db.execute(select(models.User).where(models.User.login == user_credentials.username))
    user =  query.scalars().first()
    if not user or not pwd_context.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials", 
                            headers={"WWW-Authenticate": "Basic"})
    return user