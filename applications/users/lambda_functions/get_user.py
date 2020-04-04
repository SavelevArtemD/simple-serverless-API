import json

import structlog
from pynamodb.exceptions import DoesNotExist

from applications.base.base_lambda import LambdaBase
from applications.users.db_model import UserModel
from applications.users.response_schemas import GetUserSchema

logger = structlog.get_logger()


class GetUser(LambdaBase):

    def handle(self, event, context):
        user_id = event["pathParameters"]["user_id"]
        try:
            user = UserModel.get(user_id)
            user_data = GetUserSchema().dump(user)
            return {"statusCode": 200, "body": json.dumps(user_data)}
        except DoesNotExist:
            logger.warning(f"User with id: {user_id} does not exist")
            return {"statusCode": 404, "body": None}


handler = GetUser.get_handler()
