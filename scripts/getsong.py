import requests
import argparse

# Define the playlist ID as a global variable (this is fixed)
playlist_id = "29r5ujUnrqxYr62qWcf5"

def search_song(track_name, artist_name, token):
    query = f"track:{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error in search request: {response.status_code} - {response.text}")
        return None
    response_json = response.json()
    tracks = response_json['tracks']['items']
    if tracks:
        return tracks[0]['id']
    else:
        print("No tracks found for the given song name and artist.")
    return None

def add_song_to_playlist(track_id, playlist_id, token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris=spotify:track:{track_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"  # Especifica el tipo de contenido
    }
    response = requests.post(url, headers=headers)
    
    # Imprimir la respuesta completa para entender el problema
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
    return response.status_code

def main(track_name, artist_name, token):
    track_id = search_song(track_name, artist_name, token)
    if track_id:
        status = add_song_to_playlist(track_id, playlist_id, token)
        if status == 201:
            print(f"'{track_name}' has been added to the playlist!")
        else:
            print("There was a problem with the song")
    else:
        print("Song not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add a song to the playlist')
    parser.add_argument('track_name', type=str, help='Song name')
    parser.add_argument('artist_name', type=str, help='Artist name')
    parser.add_argument('token', type=str, help="Spotify access token")

    args = parser.parse_args()

    main(args.track_name, args.artist_name, args.token)

       
