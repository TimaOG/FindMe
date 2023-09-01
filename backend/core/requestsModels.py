from pydantic import BaseModel
from datetime import datetime, date


class RegData(BaseModel):
    fio: str
    login: str
    password: str
    password2: str
    email: str
    sex: bool
    birthdate: date

class LoginData(BaseModel):
    email: str
    password: str