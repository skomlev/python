from extensions import db, BaseModel


class State(BaseModel):
    __tablename__ = 'state'

    id = db.Column(db.Integer, db.Sequence('state_id_seq'), primary_key=True)
    code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String)
