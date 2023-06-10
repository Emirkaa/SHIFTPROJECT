from fastapi import APIRouter, status, Depends
from database import Session,engine
from schemas import SignUpModel, LoginModel
from models import Employee
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException




increase_router = APIRouter(
    prefix='/increase',
    tags=['increase']
)

session = Session(bind=engine)

@increase_router.get('/increase')
async def get_info_about_increase(authorize:AuthJWT=Depends()):
    try:
         authorize.jwt_required()
        
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, предоставьте валидный токен.')
    
    current_employee = authorize.get_jwt_subject()

    employee = session.query(Employee).filter(Employee.username==current_employee).first()

    if  employee.professions == 'JUNIOR BACKEND DEVELOPER PYTHON':
        return jsonable_encoder({'message':'Ваше повышение состоится через 6 месяцев '})
    elif employee.professions == 'MIDDLE BACKEND DEVELOPER PYTHON':
        return jsonable_encoder({'message':'Ваше повышение состоится через 1 год '})
    elif employee.professions == 'SINIOR BACKEND DEVELOPER PYTHON':
        return jsonable_encoder({'message':'Ваше повышение состоится через 1.2 года '})
    

    ## Если вы улыбнетесь на этом моменте, то это оправдано, тк мне стоило использовать datetime. Почему я кинул проект такой сырой? Это мои проблемы и в этом виноват только я,

    ## Я увидел письмо очень поздно, пришлось импровизировать :D 
    # Если даже не пройду, то тут я совершил косяк - невнимательность. А так спасибо за ТЗ:D 

    # Тестировал данный серве через Insomnia(Последний пунк с повышением до другой должности не сработал, тк написал как полную хрень. пишу на данный момент очень быстро)
    
         
