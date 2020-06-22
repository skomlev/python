import csv

from api.states.models import State
from api.users.models import User
from extensions import db


def load_states_data():
    with open("states.csv", "r") as states_file:
        row_data = csv.reader(states_file)
        next(row_data)
        for row in csv.reader(states_file):
            data = row[0].split(';')
            new_state = State(code=data[0], name=data[1])
            db.session.add(new_state)
            db.session.commit()


def verify_and_create_states():
    if not State.query.first():
        load_states_data()

