from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True
