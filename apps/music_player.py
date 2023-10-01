import pyttsx3
import webbrowser
import spotipy
from spotipy import SpotifyOAuth

# Speak function
engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to play music from Spotify and open the Spotify app
def playmusiconspotify(track_name):
    try:
        # Initialize the Spotify API with your credentials
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='e7e9101e221948d0b99aeeedc1086527',
                                                       client_secret='8fbca026b1464cb6a0f65fb5c061285d',
                                                       redirect_uri='http://spotify.com',
                                                       scope='user-library-read user-read-playback-state user-modify-playback-state'))

        # Search for the track on Spotify
        results = sp.search(q=track_name, limit=1)

        if results['tracks']['items']:
            # Get the Spotify URI of the first search result (track)
            track_uri = results['tracks']['items'][0]['uri']

            # Start playback on Spotify
            sp.start_playback(uris=[track_uri])

            # Open the Spotify app
            webbrowser.open("https://open.spotify.com")

            speak(f"Playing {track_name} on Spotify and opening the Spotify app.")
        else:
            speak(f"Track {track_name} not found on Spotify.")
    except Exception as e:
        print(e)
        speak("An error occurred while playing music on Spotify.")
