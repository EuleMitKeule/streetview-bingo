from sqlalchemy.ext.hybrid import hybrid_property
from common import *
from models import add_schema, User, Game, TokenModel


@add_schema(
    users=ma.Nested(User.Schema, many=True, exclude=["token"]),
    owner=ma.Nested(User.Schema, exclude=["token"]),
    games=ma.Nested(Game.Schema, many=True)

)
class Lobby(TokenModel):
    __tablename__ = "lobby"
    users = db.relationship("User", backref="lobby", foreign_keys='User.lobby_id')
    owner = db.relationship("User", uselist=False, foreign_keys='User.owned_lobby_id')

    games = db.relationship("Game", foreign_keys="Game.lobby_id")

    def add_game(self, game: Game):
        self.games.append(game)
        if self.owner not in game.users:
            game.users.append(self.owner)
