from abc import ABC

import structlog

from services.logging import configure_logging


class LambdaBase(ABC):
    def __init__(self):
        configure_logging()
        self.logger = structlog.get_logger(f"lambda_function.{self.__class__.__name__}")

    @classmethod
    def get_handler(cls, *args, **kwargs):
        def handler(event, context):
            if isinstance(event, dict) and event.get("source") in [
                "aws.events",
                "serverless-plugin-warmup",
            ]:
                return {}
            return cls().handle(event, context)
        return handler

    def handle(self, event, context):
        raise NotImplementedError
