import os
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from dotenv import load_dotenv
from ..models import model as user_model


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):       
        return pwd_context.hash(password)

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, email: str, password: str):
    return db.query(user_model.User).filter(email = user_model.User.email).first()

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not Hash.verify_password(password, user.hashed_password):
        return False
    return user