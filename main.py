from fastapi import FastAPI 
from .databasemodels import Base

app = FastAPI()
metadata.Base.create_all(bind=engine)

app.include_router(user.routers)
app.include_router(Login.routerz)
app.include_router(blog.routers)
app.include_router(blogprofile.routers)
app.include_router(profile.routers)
app.include_routed(delete.routers)
