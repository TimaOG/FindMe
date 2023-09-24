from pydantic import BaseModel
from datetime import datetime, date
from fastapi import FastAPI, UploadFile, File


class RegDataRequest(BaseModel):
    fio: str
    login: str
    password: str
    password2: str
    email: str
    sex: bool
    birthdate: str


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


class ProjectListRequest(BaseModel):
    login: str
    email: str
    password: str
    password2: str
    oldpassword: str

class AddProjectRequest(BaseModel):
    projectName: str
    target: str
    readyState: int
    description: str
