from fastapi import FastAPI
import uvicorn



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

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)