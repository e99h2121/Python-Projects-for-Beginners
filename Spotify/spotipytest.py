import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

#https://open.spotify.com/artist/3SBG08XwrIxXSPTxsbM0b6?si=pHijf9D-QmaEvpMwgHAfoA
#https://open.spotify.com/artist/37yA8FvkJWnXZXbRg4IQaT?si=doLhjXthTCG9B3qqXYyPUg&nd=1

uri = 'spotify:artist:37yA8FvkJWnXZXbRg4IQaT'

client_id = ''
client_secret = ''
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
