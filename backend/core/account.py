from fastapi import APIRouter, Response, Request
from responseModels import BaseResponse, UserResponse
from requestsModels import UserRequest, UserSettingsRequest
from auth import verify_token, pwd_context
from database import db_get_user_info, db_save_user_info, db_delete_user, db_save_user_settings

router = APIRouter()


@router.get("/account/getAccountInfo", response_model=UserResponse, tags=["Account"])
async def get_account_info(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    user_info = db_get_user_info(decoded_data['id'])
    return user_info


@router.put("/account/saveAccountInfo", response_model=BaseResponse, tags=["Account"])
async def save_account_info(request: Request, data: UserRequest):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    db_save_user_info(data, decoded_data['id'])
    return {'header': 'OK', 'msg': ''}


@router.put("/account/saveAccountSettings", response_model=BaseResponse, tags=["Account"])
async def save_account_settings(request: Request, data: UserSettingsRequest):
    if (data.password != data.password2):
        return {'header': 'Fail', 'msg': 'Incorect password'}
    data.password = pwd_context.hash(data.password)
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    res = db_save_user_settings(data, decoded_data['id'])
    if not res:
        return {'header': 'Fail', 'msg': 'The old password is incorrect'}
    return {'header': 'OK', 'msg': ''}


@router.delete("/account/deleteAccount", response_model=BaseResponse, tags=["Account"])
async def delete_account(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    db_delete_user(decoded_data['id'])
    return {'header': 'OK', 'msg': ''}
