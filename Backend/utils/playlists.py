import spotipy
import dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

def get_playlists(sp: spotipy.Spotify):
    playlists = sp.current_user_playlists()

    playlist_dict = {playlist['name']: playlist['id'] for playlist in playlists['items']}
    return playlist_dict

dotenv.load_dotenv()

#CLIENT_ID = os.getenv('CLIENT_ID')
#CLIENT_SECRET = os.getenv('CLIENT_SECRET')
#REDIRECT_URI = 'localhost:8080'

SPOTIFY_USERNAME = 'jamiesnyders'

scope = 'user-library-read'

auth = SpotifyOAuth(scope=scope) #Creates an oauth object -> invokes access token
sp = spotipy.Spotify(auth_manager=auth)

playlist_dict = get_playlists(sp)
print(playlist_dict.keys())