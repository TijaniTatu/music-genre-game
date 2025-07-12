from flask import Flask, render_template, request, jsonify
from utils.predict import predict_genre
from utils.game import get_random_song
import os

app = Flask(__name__)

@app.route('/')
def index():
    full_path, rel_web_path, true_genre = get_random_song()
    spectrogram_path = full_path.replace("audio", "spectrograms").replace(".wav", ".png")

    return render_template("index.html", session={
        "web_song_path": rel_web_path,
        "true_genre": true_genre,
        "spectrogram": spectrogram_path
    })


@app.route('/submit', methods=['POST'])
def submit():
    user_guess = request.form.get("user_guess")
    spectrogram = request.form.get("spectrogram")
    true_genre = request.form.get("true_genre")

    ai_guess = predict_genre(spectrogram)

    result = {
        "correct_genre": true_genre,
        "user_guess": user_guess,
        "ai_guess": ai_guess,
        "user_correct": user_guess == true_genre,
        "ai_correct": ai_guess == true_genre
    }

    # Get the current song from hidden input or reload the song
    song_path = request.form.get("song_path")
    return render_template("index.html", session={
        "web_song_path": song_path,
        "true_genre": true_genre,
        "spectrogram": spectrogram,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
