from marshmallow import ValidationError

from ..models.base_model import BaseModel

def unique_validation(value, model: BaseModel, field_name: str = 'id'):
    exists = model.query.filter(getattr(model, field_name) == value).first()
    if exists:
        raise ValidationError(f"${field_name} already exists")