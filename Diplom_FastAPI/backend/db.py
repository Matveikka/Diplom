from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase


engine = create_engine("sqlite:///posts.db", echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass



