from flask_smorest import Blueprint
from flask_praetorian import auth_required as praetorian_auth_required, roles_required as praetorian_roles_required


def auth_required(func):
    func = praetorian_auth_required(func)
    func = Blueprint.doc(
        security=[
            {
                "bearerAuth": []
            }
        ]
    )(func)

    return func


def roles_required(*roles: str):

    def decorator(func):
        func = praetorian_roles_required(*roles)(func)
        func = Blueprint.doc(
            security=[
                {
                    "bearerAuth": []
                }
            ]
        )(func)

        return func

    return decorator
