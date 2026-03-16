from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db 
from sqlalchemy import Session 
from . import models 
import bcrypt
from ..models import User

router = APIRouter()

@router.post('/login')
def login(request: User, db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == request.email).first()
  password = request.password.encode("UTF-8")
  valid_password = bcrypt.checkpw(password , user.password)
  if not valid_password:
    raise HTTPException(status_code=404, detail="password not found")
  if not user:
    raise HTTPException(status_code=404, detail="email not found")
  token_data = {"user_id": user_id}
  token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
  return {
    "message": "login successful"
  }
