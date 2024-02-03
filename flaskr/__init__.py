import os

from flask import Flask, render_template, session

from . import api

from modules import game

def create_app(test_config=None):
    # create and configure flask
    app = Flask(__name__, instance_relative_config=True, template_folder="templates")
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.register_blueprint(api.api_bp)

    app.secret_key = 'TODO: changeme'

    # setup game

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # spins up an instance of the game
    @app.route('/game')
    def game_page():
        if not ("id" in session.keys()):
            id = id_count
            id_count += 1
            session["id"] = id
            games[id] = game.player(id)
            return 'Hello, World!'
        else:
            return session["id"]

    @app.route('/session')
    def sshow_session():
        return session["user"]


    @app.route("/")
    def home():
        return render_template("base.html", name = "username")


    # @app.route("/images")

    return app