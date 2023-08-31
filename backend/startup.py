from fastapi import FastAPI
import uvicorn
from core import auth
 
app = FastAPI()
 
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)