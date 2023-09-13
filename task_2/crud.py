from sqlalchemy.orm import Session
from . import models

from . import schemas


def get_user(db: Session, user_id: int):
    """ READ
    """
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def create_user(db: Session, user: schemas.UserSchema):
    """ CREATE
    """
    db_user = models.User(new_person=user.new_person)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def delete_user(db: Session, user_id: int):
    """ DELETE
    """
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return ("ok")



def update_user(db: Session, user_id: int, new_details):
    """ DELETE
    """
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    user.new_person = new_details
    db.commit()
    return ("ok")
