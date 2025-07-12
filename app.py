from flask import Flask, render_template, request, jsonify
from utils.predict import predict_genre
from utils.game import get_random_song
import os

app = Flask(__name__)

@app.route('/')
def index():
    song_path, true_genre = get_random_song()
    spectrogram_path = song_path.replace("audio", "spectrograms").replace(".wav", ".png")
    return render_template("index.html", session={
        "song_path": song_path,
        "true_genre": true_genre,
        "spectrogram": spectrogram_path
    })

@app.route('/submit', methods=['POST'])
def submit():
    user_guess = request.form["user_guess"]
    spectrogram = request.form["spectrogram"]
    true_genre = request.form["true_genre"]
    ai_guess = predict_genre(spectrogram)

    return jsonify({
        "correct_genre": true_genre,
        "user_guess": user_guess,
        "ai_guess": ai_guess,
        "user_correct": user_guess == true_genre,
        "ai_correct": ai_guess == true_genre
    })

if __name__ == "__main__":
    app.run(debug=True)
