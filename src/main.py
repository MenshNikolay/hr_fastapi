from fastapi import FastAPI
import uvicorn
from src.auth.router import user_router



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
app.include_router(user_router, prefix="/user", tags=["registration new user"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)