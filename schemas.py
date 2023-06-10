from pydantic import BaseModel
from typing import Optional
from fastapi_jwt_auth import AuthJWT
from models import Employee, Profession



class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str 
    password:str
    is_admin:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'username':'Imya',
                'secondusername':'familiya',
                'email':'xazzi.05@mail.ru',
                'password':'password',
                'is_admin':False,
                'is_active':True,
            }
        }


#Pydentic class 
class Settings(BaseModel):
    authjwt_secret_key:str = '5f1ee84bf674a26b0116cca78cd8f36ca7d9c8c93f5a41a0a542917ab521a132'


#Validate data for login
class LoginModel(BaseModel):
    username:str
    password:str


class SalaryModel(BaseModel):
    id:Optional[int]
    zarplata:int
    professions_status:Optional[str]='JUNIOR BACKEND DEVELOPER PYTHON'
    employee_id:Optional[int]


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'zarplata':150000,
                'professions_status':'JUNIOR BACKEND DEVELOPER PYTHON',
            }
        }

class IncreaseModel(BaseModel):
    id:Optional[int]
    zarplata:int
    professions_status:Optional[str]='JUNIOR BACKEND DEVELOPER PYTHON'
    employee_id:Optional[int]
