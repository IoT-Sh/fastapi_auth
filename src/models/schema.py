from pydantic import BaseModel
from typing import Union


fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Admin",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$ToeD9loZjC8Jpyce19oezuO0Q1D7oZPeg3twTRd4DXgh8dn8MTNmC",
        "disabled": False,
    },
    "admin2": {
        "username": "admin2",
        "full_name": "Admin2",
        "email": "admin2@example.com",
        "hashed_password": "$2b$12$ToeD9loZjC8Jpyce19oezuO0Q1D7oZPeg3twTRd4DXgh8dn8MTNmC",
        "disabled": False,
    }
}
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[str, None] = None
    password: str
    is_active: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

class Login(BaseModel):
    username: str
    password: str