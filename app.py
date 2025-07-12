from flask import Flask, render_template, request, jsonify
from utils.predict import predict_genre
from utils.game import get_random_song
import os
from flask import session

app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def index():
    session["user_score"] = session.get("user_score", 0)
    session["ai_score"] = session.get("ai_score", 0)
    full_path, rel_web_path, true_genre = get_random_song()
    spectrogram_path = full_path.replace("audio", "spectrograms").replace(".wav", ".png")

    return render_template("index.html", session={
        "web_song_path": rel_web_path,
        "true_genre": true_genre,
        "spectrogram": spectrogram_path
    })


@app.route('/submit', methods=['POST'])
def submit():
     # Fetch session scores or initialize
    user_score = session.get("user_score", 0)
    ai_score = session.get("ai_score", 0)

    user_guess = request.form.get("user_guess")
    spectrogram = request.form.get("spectrogram")
    true_genre = request.form.get("true_genre")

    ai_guess = predict_genre(spectrogram)

    # Score logic
    user_correct = user_guess == true_genre
    ai_correct = ai_guess == true_genre

    if user_correct:
        user_score += 1
    if ai_correct:
        ai_score += 1

    session["user_score"] = user_score
    session["ai_score"] = ai_score

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
        "result": result,
        "user_score": user_score,
        "ai_score": ai_score
    })

if __name__ == "__main__":
    app.run(debug=True)
