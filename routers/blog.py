from auth import get_active_user
from fastapi import APIRouter, Depends 
from ..databasemodels import get_db
from ..models import User
from . import models

router = APIRouter()

@router.post('/blog')
def create_blog(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  new_blog = models.Blog(name=request.name, user_id = current_user.id)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return {
    "message": "done , blog created"
  }
