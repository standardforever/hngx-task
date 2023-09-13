from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




class Person(BaseModel):
    new_person: str
  


@app.post("/api/", response_model=schemas.UserSchemaResponse)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)




@app.get("/api/{user_id}", response_model=schemas.UserSchemaResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user




@app.delete("/api/{user_id}", response_model=schemas.DeleteSchemaResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id=user_id)
    return ({"message": "User with these id = {} has been deleted successfully".format(user_id)})




@app.put("/api/{user_id}", response_model=schemas.DeleteSchemaResponse)
def read_user(user: schemas.UpdateUserSchema, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.update_user(db, user_id=user_id, new_details = user.new_details)
    return ({"message": "User with these id = {} has been updated successfully".format(user_id)})

