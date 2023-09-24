from fastapi import FastAPI
import uvicorn
from core import auth, account, projects, projectsSearch, userSearch
from core.responseModels import RootInfoResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(account.router)
app.include_router(projects.router)
app.include_router(projectsSearch.router)
app.include_router(userSearch.router)


@app.get("/", response_model=RootInfoResponse, tags=["RootLoadInfo"])
def get_root_info():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
