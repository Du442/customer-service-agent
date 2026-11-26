from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
from sqlalchemy import event
from typing import Generator
import os

load_dotenv(override=True)

path = os.getenv("DATABASE_PATH")

engine = create_engine(url=path, connect_args={"check_same_thread": False},)

def init_db() -> None:

    from agent import model

    SQLModel.metadata.create_all(engine)

@event.listens_for(engine, "connect")
def activate_foreign_keys(dbapi_conn, _):
    cur = dbapi_conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.close()

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session