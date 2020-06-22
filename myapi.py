# coding: utf-8
from api.states.utils import verify_and_create_states
from app_factory import create_app
from extensions import db

application = create_app()


with application.app_context():
    db.create_all()
    verify_and_create_states()

if __name__ == '__main__':
    host = application.config["APP_HOST"]
    port = application.config["APP_PORT"]
    application.run(host=host, port=port)
