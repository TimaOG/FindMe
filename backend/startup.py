from fastapi import FastAPI
import uvicorn
from core import auth, account, projects, projectsSearch
from core.responseModels import RootInfoResponse
 
app = FastAPI()
 
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(projects.router)
app.include_router(projectsSearch.router)

@app.get("/", response_model=RootInfoResponse, tags=["RootLoadInfo"])
def get_root_info():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)