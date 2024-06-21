from fastapi import FastAPI
import uvicorn
from src.staff.router import login_router
from src.auth.router import user_router
from fastapi.templating import Jinja2Templates



app = FastAPI(title="HR project", 
              description="Service for HR department")


@app.get("/start")
def start():
    return {
        "Title": "HR PROJECT",
        "Goal": "Provide best service on the best web frame work",
        "Reason": "Improve programing skills",
        "Author": "N.R. Mensh"
    }
app.include_router(login_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)