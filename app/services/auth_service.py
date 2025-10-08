from flask_jwt_extended import create_access_token, create_refresh_token

from ..extensions import db
from ..models.user_model import UserModel

def get_admin(identity):
    user = UserModel.query.get(identity)
    return {"admin": bool(user.admin)}

def get_user_by_email(email: str):
    query = UserModel.query.filter_by(email=email).first()
    return query

def gen_tokens(identity, fresh: bool = True):
    access_token = create_access_token(identity, fresh=fresh)
    if not fresh:
        return {"access_token": access_token}
    
    refresh_token = create_refresh_token(identity)
    return {"access_token": access_token,
            "refresh_token": refresh_token}

def register_user(username, email, password ):
    user_db = UserModel(username=username, email=email)
    user_db.password = password
    db.session.add(user_db)
    db.session.commit()
    return {
        "id": user_db.id,
        "email": user_db.email,
        "username": user_db.username
    }

def get_user_by_id(id: int):
    query = UserModel.query.filter_by(id=id).first()
    return query