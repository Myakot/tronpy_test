from sqlalchemy import Column, Integer, String
from .database import Base


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
