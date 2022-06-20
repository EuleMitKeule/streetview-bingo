from src.models import BaseModel, add_schema
from src.common import db, ma
from src.models.user import User
from src.models.utils.add_view import add_view

word_user_table = db.Table(
    "word_user", db.Model.metadata,
    db.Column("word_id", db.Integer, db.ForeignKey("words.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
)

@add_view()
@add_schema(
    users=ma.Nested(User.Schema, many=True)
)
class Word(BaseModel):
    __tablename__ = "words"

    text: str = db.Column(db.String(32), index=True)
    users: list[User] = db.relationship(User, secondary=word_user_table)
    lobby_id: int = db.Column(db.Integer, db.ForeignKey("lobbies.id"))