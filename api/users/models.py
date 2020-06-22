from api.states.models import State
from extensions import db, BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String)
    state_id = db.Column(db.Integer, db.ForeignKey(State.id))
