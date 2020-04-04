from marshmallow import fields

from applications.base.base_schema import BaseSchema


class CommentCreateSchema(BaseSchema):
    user_id = fields.String(load_only=True)
    body = fields.String(load_only=True)