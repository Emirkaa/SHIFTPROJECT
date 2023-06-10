from database import Base
from sqlalchemy import Column, Integer, Boolean, String, DECIMAL, Text, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key = True)
    username = Column(String(25))
    secondusername = Column(String(25))
    email = Column(String(30), unique=True)
    password = Column(Text, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    professions = relationship('Profession', back_populates = 'employee')

    def __repr__(self):
        return f'<Employee {self.username}'
    
class Profession(Base):
    #Профессии набросал просто для примера.
    PROFESSION_STATUSES=(('JUNIOR BACKEND DEVELOPER PYTHON','junior backend developer python'),
                         ('MIDDLE BACKEND DEVELOPER PYTHON','middle backend developer python'),
                         ('SINIOR BACKEND DEVELOPER PYTHON','sinior backend developer python'))

    __tablename__='professions'
    id = Column(Integer , primary_key=True)
    zarplata = Column(Integer, nullable=False)
    professions_status = Column(ChoiceType(choices=PROFESSION_STATUSES), default='JUNIOR BACKEND DEVELOPER PYTHON')
    employee_id = Column(Integer,ForeignKey('employee.id'))
    employee = relationship('Employee', back_populates='professions')

    def __repr__(self):
        return f'<Profession {self.id}'
