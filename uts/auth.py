from typing import Union, Tuple
from base64 import urlsafe_b64encode
from requests import post
from dotenv import dotenv_values

env = dotenv_values()

def get_access_token(code: str) -> Union[Tuple[str, int], None]:

    if not code:
        return None

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {
        "code": code,
        "redirect_uri": env["REDIRECT_URI"],
        "grant_type": "authorization_code",
        "client_id": env["CLIENT_ID"],
        "client_secret": env["CLIENT_SECRET"]
    }

    request = post("https://accounts.spotify.com/api/token", data=body, headers=headers)

    if request.status_code != 200:
        return None

    data = request.json()

    return data["access_token"], data["expires_in"]
