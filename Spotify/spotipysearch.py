import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

search = input("What do you want to search? : ")
client_id = ''
client_secret = ''
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.search(q=search, limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'], track['album']['images'][0]['url'])
