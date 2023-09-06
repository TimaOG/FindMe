from fastapi import APIRouter, Response, Request
from .responseModels import BaseResponse, UserResponse
from .requestsModels import UserRequest, UserSettingsRequest
from .auth import verify_token, pwd_context
from .database import db_get_user_info, db_save_user_info, db_delete_user, db_save_user_settings

router = APIRouter()


@router.post("/usersSearch/{page}", response_model=UserResponse, tags=["UsersSearch"])
def get_projects_list(page: int):
    pass


@router.get("/usersSearch/user/{id}", response_model=UserResponse, tags=["UsersSearch"])
def get_project_info(id: int):
    pass
