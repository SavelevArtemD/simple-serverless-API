import uuid
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, NumberAttribute

from applications.base.base_db_model import BaseModel


class CommentModel(BaseModel):
    class Meta:
        table_name = BaseModel.format_table_name("comments")

    user_id = UnicodeAttribute(hash_key=True, default_for_new=lambda: str(uuid.uuid4()))
    created_datetime = NumberAttribute(range_key=True, default_for_new=lambda: str(datetime.utcnow().timestamp()))
    body = UnicodeAttribute(null=False)
