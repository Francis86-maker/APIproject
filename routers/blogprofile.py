from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from ..models import Blog
from . import models 
from auth import get_active_user

router = APIRouter()

@router.get('/blog/me')
def get_blogs(current_user: Blog=Depends(get_active_user), db: Session=Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.user_id == current_user.id).first()
  if not blog:
    raise HTTPException(atatus_code=404, detail="blog not found")
  return blog
