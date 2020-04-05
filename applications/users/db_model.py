import uuid
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, NumberAttribute

from applications.base.base_db_model import BaseModel


class UserModel(BaseModel):
    class Meta:
        table_name = BaseModel.format_table_name("users")

    id = UnicodeAttribute(hash_key=True, default_for_new=lambda: str(uuid.uuid4()))
    username = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    date_joined = NumberAttribute(default_for_new=lambda: datetime.utcnow().timestamp())
