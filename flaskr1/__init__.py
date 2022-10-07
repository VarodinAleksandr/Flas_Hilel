import os

from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskdbc.sqlite'),
    )

    from . import db
    db.init_app(app)

    from . import track
    app.register_blueprint(track.bp)

    # app.add_url_rule('/', endpoint='index')

    return app
