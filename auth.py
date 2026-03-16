from fastapi import Depends, HTTPException 
from fastapi.security import oauth2 
from ..databasemodels import get_db
from ..models import User
from sqlalchemy import Session
from jose import jwt
from . import models 

SECRET_KEY = "secretkeypass"
ALGORITHM = "HS256"
oauth2_scheme = oauth2PasswordBearer(tokenURL="Login")

def get_active_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
  payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
  user_id = payload.get("user_id")
  user = db.query(models.User).filter(models.User.id == request.id).first()
  if not user:
    raise HTTPException(status_code=404, detail="user not found")
  return user
