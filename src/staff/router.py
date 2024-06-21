from fastapi import Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import APIRouter
from src.staff.user_operation import get_user
from src.models import User, Client
from src.staff.user_operation import get_user
from src.database import get_async_sessioon

login_router = APIRouter()
templates = Jinja2Templates(directory="src/templates")

@login_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@login_router.get("/clients", response_class=HTMLResponse)
async def read_clients(request: Request, user: User = Depends(get_user), db: AsyncSession = Depends(get_async_sessioon)):
    result = await db.execute(select(Client).where(Client.supervisor == user.fullname))
    clients = result.scalars().all()
    return templates.TemplateResponse("clients_list.html", {"request": request, "clients": clients})

@login_router.post("/clients/{client_inn}")
async def update_client_status(client_inn: int, status: str = Form(...), user: User = Depends(get_user), db: AsyncSession = Depends(get_async_sessioon)):
    result = await db.execute(select(Client).where(Client.inn == client_inn))
    client = result.scalars().first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    client.status = status
    await db.commit()
    return RedirectResponse(url="/clients", status_code=302)
