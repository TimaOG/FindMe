from fastapi import APIRouter, Response, Request
import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from core.requestsModels import RegData, LoginData
from core.responseModels import BaseResponse

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

def create_jwt_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError:
        return None


@router.post("/register", response_model=BaseResponse, tags=["Auth"])
def register_user(data:RegData):
    #hashed_password = pwd_context.hash(gg)
    # Сохраните пользователя в базе данных
    return {'header': 'OK', 'msg': ''}

@router.post("/login", response_model=BaseResponse, tags=["Auth"])
def register_user(request: Request, response: Response, data:LoginData):
    #hashed_password = pwd_context.hash(gg)
    # Сохраните пользователя в базе данных
    jwt_token = create_jwt_token({"id": 1})
    response.set_cookie(key="token", value=jwt_token)
    return {'header': 'OK', 'msg': ''}

@router.post("/test", response_model=BaseResponse, tags=["Auth"])
def register_user(request: Request, response: Response, data:LoginData):
    decoded_data = verify_jwt_token(request.cookies.get('token'))
    if decoded_data is None:
        return {'header': 'Fail', 'msg': 'FUCK YOU'}
    return {'header': 'OK', 'msg': ''}