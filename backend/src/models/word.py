from common import *
from models import BaseModel, add_schema


@add_schema(
    
)
class Word(BaseModel):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)
