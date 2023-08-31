from pydantic import BaseModel

class BaseResponse(BaseModel):
    header: str
    msg: str