from pydantic import BaseModel


class AddressInfo(BaseModel):
    bandwidth: int
    energy: int
    balance: float


class AddressRequest(BaseModel):
    address: str


class RequestLog(BaseModel):
    id: int
    address: str

    class Config:
        orm_mode = True
