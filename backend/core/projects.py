from fastapi import APIRouter, Response, Request
from .responseModels import BaseResponse, UserResponse, ProjectInfoResponse
from .requestsModels import UserRequest, UserSettingsRequest
from .auth import verify_token, pwd_context
from .database import db_get_user_info, db_save_user_info, db_delete_user, db_save_user_settings, db_get_project_info

router = APIRouter()


@router.post("/projects/{page}", response_model=UserResponse, tags=["Projects"])
def get_projects_list(page: int):
    pass


@router.get("/projects/getProject", response_model=ProjectInfoResponse, tags=["Projects"])
def get_project_info(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    user_info = db_get_project_info(decoded_data['id'])
    return user_info


@router.get("/projects/addProject", response_model=ProjectInfoResponse, tags=["Projects"])
def get_project_info(request: Request):
    pass


@router.put("/projects/editProject/{id}", response_model=UserResponse, tags=["Projects"])
def edit_project(id: int):
    pass


@router.delete("/projects/deleteProject/{id}", response_model=UserResponse, tags=["Projects"])
def delete_project(id: int):
    pass
