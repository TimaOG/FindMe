from pydantic import BaseModel


class RegData(BaseModel):
    fio: str
    login: str
    password: str
    email: str

class LoginData(BaseModel):
    email: str
    password: str