import os
import random

def get_random_song():
    base_path = "static/audio"
    genres = os.listdir(base_path)
    selected_genre = random.choice(genres)
    song_file = random.choice(os.listdir(f"{base_path}/{selected_genre}"))
    return f"{base_path}/{selected_genre}/{song_file}", selected_genre
