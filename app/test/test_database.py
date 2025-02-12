from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import RequestLog

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_create_log():
    db = TestingSessionLocal()
    log = RequestLog(address="TPs5PyUj7RZ7E5h8gPt8PcqQq2e2c9v7p7")
    db.add(log)
    db.commit()
    db.refresh(log)
    assert log.id is not None
    db.close()
