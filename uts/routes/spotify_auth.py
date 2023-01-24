from flask import Blueprint, redirect, request, make_response
from dotenv import dotenv_values
from urllib.parse import urlencode
from time import time

from ..auth import get_access_token
from ..utils import generate_random_string
from ..db import get_cursor, commit

env = dotenv_values()

spotify_auth_router = Blueprint("spotify_auth", __name__, template_folder="templates")

@spotify_auth_router.get("/login")
def login():

    params = {
        "response_type": 'code',
        "client_id": env["CLIENT_ID"],
        "scope": env["SCOPE"],
        "redirect_uri": env["REDIRECT_URI"],
    }

    params_query_string = urlencode(params)

    response = make_response(redirect(f"https://accounts.spotify.com/authorize?{params_query_string}"))

    if not request.cookies.get("session"):
        new_cookie = generate_random_string()

        cursor = get_cursor()
        cursor.execute(f"INSERT INTO users(user, access_token, expires_in, cookie) VALUES ('', '', '', ?);", (new_cookie,))

        response.set_cookie("session", new_cookie)

        commit()

    return response


@spotify_auth_router.get("/callback")
def callback():

    code = request.args.get("code")
    session = request.cookies.get("session")

    if not code:
        return "error, no code"

    if not session:
        return "error, no cookie"

    access_token, expires_in = get_access_token(code)

    cursor = get_cursor()
    cursor.execute("UPDATE users SET access_token = ?, expires_in = ? WHERE cookie = ?", (access_token, int(time() + expires_in), session))
    commit()

    return redirect("/dashboard")
