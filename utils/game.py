import os
import random

def get_random_song():
    base_path = "static/audio"
    genres = [g for g in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, g))]
    selected_genre = random.choice(genres)
    genre_path = os.path.join(base_path, selected_genre)

    songs = [f for f in os.listdir(genre_path) if f.endswith(".wav")]
    selected_song = random.choice(songs)

    full_path = os.path.join(genre_path, selected_song)  # static/audio/rock/rock1.wav
    relative_path = full_path.replace("static/", "")      # audio/rock/rock1.wav

    return full_path, relative_path, selected_genre
