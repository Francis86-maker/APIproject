from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from ..models import User 
from ..auth import get_active_user
from . import models 

router = APIRouter()

@router.delete('/delete')
def delete_user(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  current_user = db.query(models.User).filter(models.User.id == request.id)
  if not current_user:
    raise HTTPException(status_code=404, detail="user not found")
  current_user.delete(synchronized_session=False)
  return {
   "message": "user successfully deleted"
  }
