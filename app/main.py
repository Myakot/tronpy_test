from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, services

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/address/", response_model=schemas.AddressInfo)
async def get_address_info(
    request: schemas.AddressRequest, db: Session = Depends(get_db)
):
    if not request.address:
        raise HTTPException(status_code=400, detail="Address is required")
    info = await services.get_info_by_address(request.address, db)
    return info


@app.get("/logs/", response_model=list[schemas.RequestLog])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logs = services.get_logs(db, skip=skip, limit=limit)
    return logs
