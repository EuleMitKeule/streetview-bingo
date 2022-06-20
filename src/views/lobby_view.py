import logging
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from src.common import api, ma
from src.models import User, Lobby


bp: Blueprint = Blueprint("lobbies_by_token", "lobbies_by_token", url_prefix="/api/lobbies")


class GetQuerySchema(ma.Schema):
    token: str = ma.Str(required=True)


@bp.route("/<string:token>")
class LobbiesView(MethodView):

    @bp.response(200, Lobby.Schema())
    @bp.doc(operationId="readLobbyByToken")
    def get(self, token: str):
        lobby: Lobby = Lobby.where(token=token).first()
        return jsonify(Lobby.dump(lobby))


api.register_blueprint(bp)
