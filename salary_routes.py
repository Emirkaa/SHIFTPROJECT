from fastapi import APIRouter, Depends, status
from schemas import SalaryModel
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from database import Session, engine
from models import Employee, Profession



salary_router = APIRouter(
    prefix = "/salaries",
    tags=['salaries']
)

session = Session(bind=engine)

@salary_router.get('/')
async def hello(authorize:AuthJWT=Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, введите валидный токен доступа(access_token)')
    
    return jsonable_encoder({'message':'Hello'})


@salary_router.post('/salary', status_code=status.HTTP_201_CREATED)
async def place_current_salary(salary:SalaryModel,authorize:AuthJWT=Depends()):

    """
        ## Вписать текущую заработную плату в месяц для текущей должности.
        - zarplata:int
        - professions_status:str
        
    """


    try:
        authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, предоставьте валидный токен доступа')
    current_employee = authorize.get_jwt_subject()

    employee = session.query(Employee).filter(Employee.username == current_employee).first()


    save_salary = Profession(
        professions_status=salary.professions_status,
        zarplata=salary.zarplata
    )

    save_salary.employee = employee

    session.add(save_salary)
    session.commit()

    answer = {
        'professions_status':save_salary.professions_status,
        'zarplata':save_salary.zarplata
    }
    return jsonable_encoder(answer)


@salary_router.get('/info_about_employs')
async def list_all_salaries_before_the_increase(authorize:AuthJWT=Depends()):
    """
        ## Список всех зп сотрудника за все время работы в компании.
    """
    try:
        authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пожалуйста, предоставьте валидный токен доступа')
    
    current_employee = authorize.get_jwt_subject()

    employee = session.query(Employee).filter(Employee.username==current_employee).first()

    if employee.is_admin:
        salaries = session.query(Profession).all()
        return jsonable_encoder(salaries)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Вы не администратор.')










    


