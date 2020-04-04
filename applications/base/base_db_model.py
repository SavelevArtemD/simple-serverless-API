import os

from pynamodb.models import Model


class BaseModel(Model):
    class Meta:
        table_name: str = NotImplemented

    @staticmethod
    def format_table_name(simple_table_name: str) -> str:
        return f"{os.environ['STAGE']}-{simple_table_name}"
