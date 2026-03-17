from pydantic import BaseModel 

class Blog(BaseModel):
  name: str
class User(BaseModel):
  email: str
  name: str
  password: str
