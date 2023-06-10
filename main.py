from fastapi import FastAPI
from auth_routes import auth_router
from salary_routes import salary_router
from increase import increase_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings


app = FastAPI()

@AuthJWT.load_config
def get_config():return Settings()


app.include_router(auth_router)
app.include_router(salary_router)
app.include_router(increase_router)




