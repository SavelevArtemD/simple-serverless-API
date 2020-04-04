from marshmallow import fields

from applications.base.base_schema import BaseSchema


class GetUserSchema(BaseSchema):
    id = fields.String(dump_only=True)
    username = fields.String(dump_only=True)
    email = fields.String(dump_only=True)
    date_joined = fields.Number(dump_only=True)
