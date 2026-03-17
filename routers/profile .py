from fastapi import APIRouter, Depends, HTTPException 
from ..models import User 
from ..databasemodels import get_db
from . import models 
from ..auth import get_active_user

router = APIRouter()

@router.get('/user/me')
def get_user(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  current_user = db.query(models.User).filter(models.User.id == request.id).first()
  if not user:
    raise HTTPException (status_code=404, detail="User not found")
  return current_user
