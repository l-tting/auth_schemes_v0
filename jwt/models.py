from sqlalchemy import Column,Integer,String
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String(100),nullable=False)
    email = Column(String(50),nullable=False,unique=True)
    password = Column(String(200),nullable=False)