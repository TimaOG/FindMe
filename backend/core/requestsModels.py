from pydantic import BaseModel
from datetime import datetime, date


class RegDataRequest(BaseModel):
    fio: str
    login: str
    password: str
    password2: str
    email: str
    sex: bool
    birthdate: date

class LoginDataRequest(BaseModel):
    email: str
    password: str

class UserRequest(BaseModel):
    description: str
    achievements: str
    education: str
    professionList: list[int] = []
    hobbyList: list[int] = []

class UserSettingsRequest(BaseModel):
    login: str
    email: str
    password: str
    password2: str
    oldpassword: str