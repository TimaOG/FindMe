from fastapi import APIRouter, Response, Request
from responseModels import BaseResponse, UserResponse
from requestsModels import UserRequest, UserSettingsRequest
from auth import verify_token, pwd_context
from database import db_get_user_info, db_save_user_info, db_delete_user, db_save_user_settings

router = APIRouter()


@router.post("/projects/{page}", response_model=UserResponse, tags=["Projects"])
def get_projects_list(page: int):
    pass


@router.post("/projects/addProject", response_model=UserResponse, tags=["Projects"])
def get_project_info(id: int):
    pass


@router.put("/projects/editProject/{id}", response_model=UserResponse, tags=["Projects"])
def edit_project(id: int):
    pass


@router.delete("/projects/deleteProject/{id}", response_model=UserResponse, tags=["Projects"])
def delete_project(id: int):
    pass
