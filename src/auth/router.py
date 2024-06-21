from fastapi import FastAPI, Depends, HTTPException,APIRouter
from src import models
from src.staff.user_operation import transform_pwd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth import schemas
from src.database import get_async_sessioon
from src.auth.schemas import UserResponse, ClientResponse

user_router = APIRouter()



@user_router.post("/new_user", response_model=UserResponse)
async def  create_new_user(user: schemas.UserCreate, 
                    db: AsyncSession = Depends(get_async_sessioon)):
    result = await db.execute(select(models.User).filter(models.User.login == user.login))
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


@user_router.post("/new_client", response_model=ClientResponse)
async def create_new_client(client: schemas.ClientCreate, 
                            db: AsyncSession = Depends(get_async_sessioon)):
    result = await db.execute(select(models.Client).filter(models.Client.inn == client.inn))
    db_client = result.scalars().first()

    if db_client:
        raise HTTPException(status_code=400, detail="I know this client. I've enrolled it.")
    new_client = models.Client(
        account_number = client.account_number,
        name = client.name,
        surname = client.surname,
        father_name = client.father_name,
        b_day = client.b_day,
        inn = client.inn,
        supervisor = client.supervisor,
        status = client.status,
    )
    db.add(new_client)
    await db.commit()
    await db.refresh(new_client)
    client_response = ClientResponse.from_orm(new_client)
    return client_response
'''
@user_router.post("/auth")
async def login_user(db: AsyncSession = Depends(get_async_sessioon),
    login: str
)
'''