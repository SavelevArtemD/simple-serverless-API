import json
import logging.config
import sys
import structlog
from structlog.contextvars import merge_contextvars


def configure_logging():
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.DEBUG)
    renderer = structlog.processors.JSONRenderer(serializer=json.dumps)
    structlog.configure(
        processors=[
            merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.format_exc_info,
            renderer,
        ],
        wrapper_class=structlog.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=False
    )
