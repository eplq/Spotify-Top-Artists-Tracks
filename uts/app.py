from flask import Flask, render_template

from .db import setup
from .routes.spotify_auth import spotify_auth_router
from .routes.user_tops import user_tops_router

def create_app():
    app = Flask(__name__)
    setup()

    app.register_blueprint(spotify_auth_router)
    app.register_blueprint(user_tops_router)

    @app.route("/")
    def index():
        return render_template("index.html")

    print(app.url_map)

    return app
