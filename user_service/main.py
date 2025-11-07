from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4
from database import async_session
from models.user_model import User
from schemas.user_schema import UserCreate, UserRead

app = FastAPI()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@app.post("/users", response_model=UserRead)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = User(id=str(uuid4()), name=user.name, email=user.email)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
