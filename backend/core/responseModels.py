from pydantic import BaseModel
from datetime import datetime, date

class BaseResponse(BaseModel):
    header: str
    msg: str

class UserResponse(BaseModel):
    fio: str
    birthdate: str
    sex: bool
    description: str
    achievements: str
    education: str
    email: str
    professionList: list[str] = []
    hobbyList: list[str] = []

