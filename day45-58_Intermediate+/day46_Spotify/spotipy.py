import spotipy
from spotipy.oauth2 import SpotifyOAuth

# from spotipy.oauth2 import SpotifyOAuth

# OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
# OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

# scope = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])