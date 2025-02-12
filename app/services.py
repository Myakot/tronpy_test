from tronpy import Tron
from sqlalchemy.orm import Session
from . import models, schemas
import re


async def get_info_by_address(address: str, db: Session):
    if not re.match(r"^T[a-zA-Z0-9]{33}$", address):
        raise ValueError("Invalid Tron address format")

    client = Tron()
    account = client.get_account(address)

    bandwidth = account.get("free_net_usage", 0) + account.get("net_usage", 0)
    energy = account.get("energy_usage", 0)
    balance = account.get("balance", 0) / 1_000_000

    log = models.RequestLog(address=address)
    db.add(log)
    db.commit()
    db.refresh(log)

    return schemas.AddressInfo(bandwidth=bandwidth, energy=energy, balance=balance)


def get_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RequestLog).offset(skip).limit(limit).all()
