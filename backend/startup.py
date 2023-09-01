from fastapi import FastAPI
import uvicorn
from core import auth, account
 
app = FastAPI()
 
app.include_router(auth.router)
app.include_router(account.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)