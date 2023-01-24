# Learning how to use the Spotify Auth

This is a learning project, which can be considered as an example of how to authenticate the user with the Spotify API.

It is a simple but functional app that shows you your top 20 tracks and artists of the last 6 months.

## How to use

First clone the repository and enter the directory:

```sh
git clone https://github.com/eplq/Spotify-Top-Artists-Tracks.git
cd Spotify-Top-Artists-Tracks
```

Login in the [Spotify Developer Portal](https://developer.spotify.com/dashboard) and create an application, then write the values in the .env file (use [.env.example](./.env.example) as template):

```env
CLIENT_ID=<your client id>
CLIENT_SECRET=<your client secret>
REDIRECT_URI=<the redirect uri>
SCOPE=user-top-read
```

Then, create a Python virtual environment and install the dependencies:

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Finally, run the app:

```sh
flask --app uts.app --debug run
```

## License

See [LICENSE](./LICENSE)
