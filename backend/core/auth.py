from fastapi import APIRouter, Response, Request
import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from core.requestsModels import RegDataRequest, LoginDataRequest
from core.responseModels import BaseResponse
from core.database import db_create_user, db_check_user_in_system_by_email_and_login, db_check_user_in_system

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

def create_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def refresh_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


@router.post("/register", response_model=BaseResponse, tags=["Auth"])
async def register_user(data:RegDataRequest):
    if(data.password != data.password2):
        return {'header': 'Fail', 'msg': 'Incorect password'}
    data.password = pwd_context.hash(data.password)
    checker = db_check_user_in_system_by_email_and_login(data.email, data.login)
    if(not checker[0]):
        return {'header': 'Fail', 'msg': checker[1]}
    db_create_user(data)
    return {'header': 'OK', 'msg': ''}

@router.post("/login", response_model=BaseResponse, tags=["Auth"])
async def login_user(request: Request, response: Response, data:LoginDataRequest):
    checkData = db_check_user_in_system(data)
    if not checkData[0]:
        return {'header': 'Fail', 'msg': 'User does not exist'}
    jwt_token = create_token({"id": checkData[2]})
    if pwd_context.verify(data.password, checkData[1]):
        response.set_cookie(key="token", value=jwt_token)
        return {'header': 'OK', 'msg': ''}
    return {'header': 'Fail', 'msg': 'Password is wrong'}

@router.get("/logout", response_model=BaseResponse, tags=["Auth"])
async def logout_user(response: Response):
    response.delete_cookie("token")
    return {'header': 'OK', 'msg': ''}
