from fastapi import APIRouter, Response, Request
from .responseModels import BaseResponse, UserResponse
from .requestsModels import UserRequest, UserSettingsRequest
from .auth import verify_token, pwd_context
from .database import db_get_user_info, db_save_user_info, db_delete_user, db_save_user_settings, db_save_user_ava_info, db_save_user_resume_info
from fastapi import FastAPI, UploadFile, File
import shutil
import os

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

@router.put("/account/saveAccountAvatar", response_model=BaseResponse, tags=["Account"])
async def save_account_avatar(request: Request, file: UploadFile = File(...)):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    first_four_bytes = await file.read(8)
    await file.seek(0)
    if not first_four_bytes[:2] in [b'\xff\xd8', b'\x89P', b'BM', b'II*\x00', b'MM\x00*']:
        return {'header': 'Fail', 'msg': 'File is not supported'}
    oldName = db_save_user_ava_info(file.filename, decoded_data['id'])
    if oldName != '' or oldName != None:
        if os.path.isfile('backend/core/files/user' + str(decoded_data['id']) + '/' + oldName):
            os.remove('backend/core/files/user' + str(decoded_data['id']) + '/' + oldName)
    with open('backend/core/files/user' + str(decoded_data['id']) + '/' + file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'header': 'OK', 'msg': ''}

@router.put("/account/saveAccountResume", response_model=BaseResponse, tags=["Account"])
async def save_account_resume(request: Request, file: UploadFile = File(...)):
    decoded_data = verify_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'Access denied'}
    first_four_bytes = await file.read(4)
    await file.seek(0)
    if first_four_bytes != b'%PDF':
        return {'header': 'Fail', 'msg': 'File is not supported'}
    oldName = db_save_user_resume_info(file.filename, decoded_data['id'])
    if oldName != '' or oldName != None:
        if os.path.isfile('backend/core/files/user' + str(decoded_data['id']) + '/' + oldName):
            os.remove('backend/core/files/user' + str(decoded_data['id']) + '/' + oldName)
    with open('backend/core/files/user' + str(decoded_data['id']) + '/' + file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
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
