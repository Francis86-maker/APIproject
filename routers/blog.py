from auth import get_active_user
from fastapi import APIRouter, Depends 
from ..databasemodels import get_db
from ..models import User
from . import models

router = APIRouter()

@router.post('/blog')
def get_active_user(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  new_blog = db.query(models.User).filter(models.User.id == request.idl).first()
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return {
    "message": "done , blog created"
  }
