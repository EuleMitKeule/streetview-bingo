from marshmallow import EXCLUDE, post_load
from common import *


def add_schema(**kwargs):
    
    def decorator(cls):
        class Meta:
            model = cls
            load_instance = True
            unknown = EXCLUDE
            sqla_session = db.session

        if "meta" in kwargs:
            for key, value in kwargs.get("meta").items():
                setattr(Meta, key, value)

            kwargs.pop("meta")

        name: str = kwargs.pop("name") if "name" in kwargs else "Schema"

        schema = type("Schema", (ma.SQLAlchemyAutoSchema,), {
            "Meta": Meta,
            **kwargs
        })

        setattr(cls, name, schema)
        return cls

    return decorator
