from database import engine, Base
from models import Employee, Profession

Base.metadata.create_all(bind=engine)




