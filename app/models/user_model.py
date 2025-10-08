from .base_model import BaseModel
from ..extensions import db, bcrypt

class UserModel(BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def password(self):
        raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self, plain):
        self._password = bcrypt.generate_password_hash(plain).decode("utf-8")

    def verify_password(self, plain):
        return bcrypt.check_password_hash(self._password, plain)