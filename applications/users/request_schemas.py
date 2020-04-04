from marshmallow import fields

from applications.base.base_schema import BaseSchema


class UserCreateSchema(BaseSchema):
    username = fields.String(load_only=True)
    email = fields.String(load_only=True)
