from sqlalchemy import Column, Integer, String, Date, ForeignKey,MetaData,BigInteger, Enum as SQLENUM
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum


metadata = MetaData()
Base = declarative_base(metadata=metadata)

class StatusEnum(str, Enum):
    unprocessing = "Не в работе"
    processing = "В работе"
    denied = "Отказ"
    closed = "Сделка закрыта"

class User(Base):
    __tablename__ = "user"

    
    fullname = Column( String, nullable=False, primary_key=True)
    login = Column( String, nullable=False)
    hashed_password = Column( String, nullable=False)


class Client(Base):
    __tablename__ = "clients"

    account_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    b_day = Column(Date, nullable = False)
    inn = Column(BigInteger, primary_key=True, index=True)
    supervisor = Column(ForeignKey(User.fullname))
    status = Column(SQLENUM(StatusEnum), default=StatusEnum.unprocessing) 


