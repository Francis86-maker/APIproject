from sqlalchemy.orm import relationship , sessionmaker 
from sqlalchemy import  Column, String, Integer,ForeignKey
from database import declarative_base

engine = create_engine("sqlite///:blog.db", echo=True)
SessionLocal= sessionmaker(autocommit= False, autoFlush= False, bind=engine)

Base = declarative_base()
class Blog(Base):
  __tablename__="blogs"
  id = Column(Integer, primarykey=True, unique=True)
  name = Column(String)
  user_id = Column(Integer, ForeignKey("Users.id"))
  creator = relationship("User", back_populates="blog")

class User(Base):
  __tablename__= "Users"
  id = Column(Integer, primarykey=True, unique=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)
  blog = relationship("Blog", back_populates="creator")
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
  
