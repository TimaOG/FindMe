from fastapi import APIRouter, Response, Request
from core.responseModels import BaseResponse, UserResponse
from core.requestsModels import UserRequest
from core.auth import verify_token
from core.database import db_get_user_info, db_save_user_info
router = APIRouter()

@router.get("/account/getAccountInfo", response_model=UserResponse, tags=["Account"])
async def get_account_info(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    user_info = db_get_user_info(decoded_data['id'])
    return user_info

@router.post("/account/saveAccountInfo", response_model=BaseResponse, tags=["Account"])
async def save_account_info(request: Request, data: UserRequest):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    db_save_user_info(data, decoded_data['id'])
    return {'header': 'OK', 'msg': ''}

@router.post("/account/saveAccountSettings", response_model=BaseResponse, tags=["Account"])
async def save_account_settings(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    return {'header': 'OK', 'msg': ''}

@router.delete("/account/deleteAccount", response_model=BaseResponse, tags=["Account"])
async def delete_account(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    return {'header': 'OK', 'msg': ''}