from glob import glob
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: Optional[int] = 0
    password: str
    admin: bool = Field(default=False)


session: Session = None
def created_tb():
    global session
    try:
        db_url = "sqlite:///app.db"
        engine = create_engine(db_url, echo=True)
        return Session(engine)
    except Exception as e:
        return None