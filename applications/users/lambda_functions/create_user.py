import json

import structlog

from applications.base.base_lambda import LambdaBase
from applications.users.db_model import UserModel
from applications.users.request_schemas import UserCreateSchema

logger = structlog.getLogger(__name__)


class CreateUser(LambdaBase):

    def handle(self, event, context):
        new_user_data = UserCreateSchema().loads(event["body"])
        user = UserModel(
            username=new_user_data["username"],
            email=new_user_data["email"]
        )
        user.save()
        logger.debug("User created", user_id=user.id)
        return {"statusCode": 200, "body": json.dumps({"user_id": str(user.id)})}


handler = CreateUser().get_handler()
