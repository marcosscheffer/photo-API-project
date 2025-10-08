from marshmallow import fields, validates

from ..extensions import ma
from ..models.user_model import UserModel
from ..validations.unique_validation import unique_validation

class RegisterUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('email', 'username', 'password')

    email = fields.Email(required=True, load_only=True)
    username = fields.String(required=True, load_only=True)
    password = fields.String(required=True, load_only=True)

    @validates('email')
    def email_validate(self, value, **kwargs):
        unique_validation(value, UserModel, 'email')


class LoginUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('id', 'email', 'password')

    id = fields.Int(required=True, dump_only=True)
    email = fields.Email(required=True, load_only=True)
    password = fields.String(required=True, load_only=True)