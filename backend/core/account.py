from fastapi import APIRouter, Response, Request
from core.responseModels import BaseResponse, UserResponse
from core.requestsModels import LoginData
from core.auth import verify_token
from core.database import get_user_info
router = APIRouter()

@router.get("/account/getAccountInfo", response_model=UserResponse, tags=["Account"])
async def get_account_info(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access Denaid'}
    user_info = get_user_info(decoded_data['id'])
    return {'header': 'OK', 'msg': ''}

@router.post("/account/saveAccountInfo", response_model=BaseResponse, tags=["Account"])
async def save_account_info(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access Denaid'}
    return {'header': 'OK', 'msg': ''}

@router.post("/account/saveAccountSettings", response_model=BaseResponse, tags=["Account"])
async def save_account_settings(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access Denaid'}
    return {'header': 'OK', 'msg': ''}

@router.delete("/account/deleteAccount", response_model=BaseResponse, tags=["Account"])
async def delete_account(request: Request):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access Denaid'}
    return {'header': 'OK', 'msg': ''}