from flask import Blueprint, render_template, request, redirect
from time import time

from ..db import get_cursor
from ..tops import get_user_top_artists, get_user_top_songs

user_tops_router = Blueprint("user_tops", __name__)

@user_tops_router.get("/dashboard")
def dashboard():

    session = request.cookies.get("session")

    cursor = get_cursor()
    cursor.execute("SELECT access_token, expires_in FROM users WHERE cookie = ?", (session,))
    row = cursor.fetchone()

    if not row:
        return redirect("/login")

    if row["expires_in"] < time():
        return redirect("/login")

    top_artists = get_user_top_artists(row["access_token"])
    top_songs = get_user_top_songs(row["access_token"])

    return render_template("dashboard.html", top_artists=top_artists, top_songs=top_songs)
