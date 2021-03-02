from config import db
from models import User
import services.token_service as token_service

def create_user(name):
    
    token = token_service.generate_token(16)
    user = User(name=name, token=token)

    db.session.add(user)
    db.session.commit()

    return user