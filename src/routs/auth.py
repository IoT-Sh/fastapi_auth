from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..dependencies.user import *
from ..models import schema as user_schema
from ..models import model as user_model
from ..models.config import conn
from ..models.model import users

api = APIRouter()


@api.post("/token", response_model=user_schema.Token, tags=["Authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(user_schema.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@api.post("/login", response_model=user_schema.Token, tags=["Authentication"])
async def login_for_token(login_data: user_schema.Login):
    user = authenticate_user(user_schema.fake_users_db, login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@api.post("/signup", response_model=user_schema.User, tags=["Authentication"])
async def user_register(user_data: user_schema.User):
    hashed_password = get_password_hash(user_data.password)
    conn.execute(users.insert().values(
        email = user_data.email,
        first_name = user_data.first_name,
        last_name = user_data.last_name,
        hashed_password = hashed_password
    ))
    return conn.execute(users.select()).fetchall()


@api.get("/users/me/", response_model=user_schema.User, tags=["Authentication"])
async def read_users_me(current_user: user_schema.User = Depends(get_current_active_user)):
    return current_user


@api.get("/users/me/items/", tags=["Authentication"])
async def read_own_items(current_user: user_schema.User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
