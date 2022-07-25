from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, StatementError

engine = create_engine('sqlite:///aplicacion.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
