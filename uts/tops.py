from requests import get

def get_user_top_artists(access_token: str):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = get("https://api.spotify.com/v1/me/top/artists", headers=headers)

    if response.status_code != 200:
        return None

    return response.json()


def get_user_top_songs(access_token: str):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = get("https://api.spotify.com/v1/me/top/tracks", headers=headers)

    if response.status_code != 200:
        return None

    return response.json()
