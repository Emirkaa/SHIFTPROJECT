from fastapi import APIRouter, status, Depends
from database import Session,engine
from schemas import SignUpModel, LoginModel
from models import Employee
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException




auth_router = APIRouter(
    prefix='/authentication',
    tags=['auth']
)

session = Session(bind=engine)


@auth_router.get('/')
async def hello(authorize:AuthJWT=Depends()):
    try:
         authorize.jwt_required()
        
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, предоставьте валидный токен.')
    
    return {'message':f'hello world'}


@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(employee:SignUpModel):
    db_email = session.query(Employee).filter(Employee.email==employee.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Сотрудник с данным электронным адресом уже существует ')
    

    new_employee=Employee(
        username=employee.username,
        email=employee.email,
        password=generate_password_hash(employee.password),
        is_active=employee.is_active,
        is_admin=employee.is_admin
    )

    session.add(new_employee)
    session.commit()
    
    return new_employee

@auth_router.post('/login')
async def login(employee:LoginModel, authorize:AuthJWT=Depends()):
        db_employee=session.query(Employee).filter(Employee.username==employee.username).first()

        if db_employee and check_password_hash(db_employee.password,employee.password): 
            access_token = authorize.create_access_token(subject=db_employee.username)
            refresh_token = authorize.create_refresh_token(subject=db_employee.username)

            response = {
                 'access':access_token,
                 'refresh':refresh_token
            }
            return jsonable_encoder(response)
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Пожалуста, проверьте ваше Имя или пароль.')

@auth_router.get('/new_access_token')
async def refresh_token(authorize:AuthJWT=Depends()):
     try:
          authorize.jwt_refresh_token_required()

     except Exception as e:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, предоставьте валидный токен обновления(refresh_token)')
     
     current_employee = authorize.get_jwt_subject()

     new_access_token = authorize.create_access_token(subject=current_employee)

     return jsonable_encoder({'new_access_token':new_access_token})
                     



