from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()
users = {}


class User(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    user_id = str(uuid4())
    users[user_id] = user
    return {"id": user_id, "user": user}


@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
