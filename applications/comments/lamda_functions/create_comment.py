import structlog

from applications.base.base_lambda import LambdaBase
from applications.comments.db_model import CommentModel
from applications.comments.request_schemas import CommentCreateSchema

logger = structlog.getLogger(__name__)


class CreateComment(LambdaBase):
    def handle(self, event, context):
        new_comment_data = CommentCreateSchema().loads(event["body"])
        comment = CommentModel(
            user_id=new_comment_data["user_id"], body=new_comment_data["body"]
        )
        comment.save()
        logger.debug(
            "Comment created",
            user_id=comment.user_id,
            created_datetime=comment.created_datetime,
        )
        return {"statusCode": 204}


handler = CreateComment().get_handler()
