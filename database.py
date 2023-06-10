from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



engine = create_engine('postgresql://postgres:1232323@localhost/SHIFTPROJECT',
                       echo=True)


Base = declarative_base()

Session = sessionmaker()