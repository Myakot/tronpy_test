from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import RequestLog

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_create_log():
    db = TestingSessionLocal()
    log = RequestLog(address="TMY19SeunpGTRoxB1yCF1EBeZjcGNy3333")
    db.add(log)
    db.commit()
    db.refresh(log)
    assert log.id is not None
    db.close()
