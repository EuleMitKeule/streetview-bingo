from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from src.common import api, ma
from src.models import User, Lobby


bp: Blueprint = Blueprint("join", "join", url_prefix="/api/join")


class JoinQuerySchema(ma.Schema):
    token: str = ma.Str(required=True)


@bp.route("")
class JoinView(MethodView):

    @bp.response(200, Lobby.Schema())
    @bp.arguments(User.Schema, location="json")
    @bp.arguments(JoinQuerySchema, location="query")
    @bp.doc(operationId="joinLobby")
    def post(self, user: User, args: dict):
        lobby: Lobby = Lobby.where(token=args["token"]).first()

        if not lobby:
            return jsonify({"error": "Lobby not found"}), 404
        lobby.add_user(user)
        print(lobby.users)
        return jsonify(Lobby.dump(lobby))


api.register_blueprint(bp)
