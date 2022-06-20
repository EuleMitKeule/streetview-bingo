from src.common import db, ma


def add_schema(**kwargs):
    
    def decorator(cls):
        schema_name: str = f"{cls.upper_singular_name}Schema"

        class Meta:
            model = cls
            load_instance = True
            sqla_session = db.session

        if "meta" in kwargs:
            for key, value in kwargs.get("meta").items():
                setattr(Meta, key, value)

            kwargs.pop("meta")

        name: str = kwargs.pop("name", "Schema")

        schema = type(schema_name, (ma.SQLAlchemyAutoSchema,), {
            "Meta": Meta,
            # "id": ma.Integer(dump_only=True),
            **kwargs
        })

        setattr(cls, name, schema)
        return cls

    return decorator