from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from spotipy.oauth2 import SpotifyOAuth
from django.http import JsonResponse
import spotipy
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def hogwarts_house(request):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri=REDIRECT_URI,
                                                    scope='user-top-read'))

    try:
        top_artists = sp.current_user_top_artists(time_range='medium_term', limit=400)

        # Extract genres from artists and count them
        genres_count = {}
        for artist in top_artists['items']:
            for genre in artist['genres']:
                genres_count[genre] = genres_count.get(genre, 0) + 1

        # Sort genres by count
        sorted_genres = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)

        print("Your Top Genres:")
        print("----------------")
        for genre, count in sorted_genres:
            print(f"{genre} - {count} artists")
        print()

        # Extract genres from artists and count them
        genres_count = {}
        for artist in top_artists['items']:
            for genre in artist['genres']:
                genres_count[genre] = genres_count.get(genre, 0) + 1

    # Define genre-to-house mapping
        genre_house_mapping = {
        'punk': 'Gryffindor',
        'alternative': 'Gryffindor',
        'emo': 'Gryffindor',
        'rock': 'Gryffindor',
        'indie': 'Gryffindor',
        'power': 'Gryffindor',
        'garage': 'Gryffindor',
        'grungegaze': 'Gryffindor',
        'boston rock': 'Gryffindor',
        'australian garage punk': 'Gryffindor',
        'alternative metal': 'Gryffindor',
        # Hufflepuff
        'acoustic': 'Hufflepuff',
        'country': 'Hufflepuff',
        'pop': 'Hufflepuff',
        'singer-songwriter': 'Hufflepuff',
        'bubblegum': 'Hufflepuff',
        'folk': 'Hufflepuff',
        'reggae': 'Hufflepuff',
        'world': 'Hufflepuff',
        'calypso': 'Hufflepuff',
        'chill': 'Hufflepuff',
        'filmi': 'Hufflepuff',
        'k-pop': 'Hufflepuff',
        'latino': 'Hufflepuff',
        # Ravenclaw
        'classical': 'Ravenclaw',
        'jazz': 'Ravenclaw',
        'blues': 'Ravenclaw',
        'ambient': 'Ravenclaw',
        'new age': 'Ravenclaw',
        'world music': 'Ravenclaw',
        'experimental': 'Ravenclaw',
        'electronic': 'Ravenclaw',
        'psychedelic': 'Ravenclaw',
        'progressive': 'Ravenclaw',
        'shoegaze': 'Ravenclaw',
        'art pop': 'Ravenclaw',
        'dream': 'Ravenclaw',
        'new wave': 'Ravenclaw',
        'indie soul': 'Ravenclaw',
        'noise pop': 'Ravenclaw',
        'modern alternative rock': 'Ravenclaw',
        'riot grrrl': 'Ravenclaw',
        'ethereal wave': 'Ravenclaw',
        'synthpop': 'Ravenclaw',
        'trip hop': 'Ravenclaw',
        'dreamgaze': 'Ravenclaw',
        # Slytherin
        'rap': 'Slytherin',
        'hip hop': 'Slytherin',
        'trap': 'Slytherin',
        'darkwave': 'Slytherin',
        'industrial': 'Slytherin',
        'metal': 'Slytherin',
        'hardcore': 'Slytherin',
        'goth': 'Slytherin',
        'alternative metal': 'Slytherin',
        'black metal': 'Slytherin',
        'nu metal': 'Slytherin',
        'rap metal': 'Slytherin',
        'atl hip hop': 'Slytherin',
        'pluggnb': 'Slytherin',
        'rage rap': 'Slytherin',
        'chicago rap': 'Slytherin',
        'sacramento indie': 'Slytherin',
        'slap house': 'Slytherin',
        'cali rap': 'Slytherin',
        'dark pop': 'Slytherin',
        'alternative r&b': 'Slytherin',
        'escape room': 'Slytherin',
        'lgbtq+ hip hop': 'Slytherin',
        'drill': 'Slytherin',
        'chicago bop': 'Slytherin',
        'chicago drill': 'Slytherin',
        'southern hip hop': 'Slytherin',
        }

        # Calculate the house with the most representation
        house_count = {'Gryffindor': 0, 'Hufflepuff': 0, 'Ravenclaw': 0, 'Slytherin': 0}
        for genre, count in genres_count.items():
            for keyword, house in genre_house_mapping.items():
                if keyword in genre.lower():
                    house_count[house] += count

    # Determine the house with the highest count
        sorted_houses = sorted(house_count.items(), key=lambda x: x[1], reverse=True)
        most_likely_house = sorted_houses[0][0]
        print("HALO")
        print("Based on your music style, you would be in the", most_likely_house, "house!")
        print(house_count)
        response_data = {
            "house": most_likely_house,
            "house_count": house_count
        }
    
        house = most_likely_house  # Replace with the actual Hogwarts house

        return JsonResponse({'house': house})
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 403 and e.code == -1:
            # Token might be expired, try refreshing
            sp.refresh_access_token(sp.auth_manager.get_cached_token()['refresh_token'])
        else:
            # Handle other errors
            print("Error:", e)
def home(request):
    return render(request, 'home.html')
