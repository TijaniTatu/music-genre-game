import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def generate_spectrogram(audio_path, output_path):
    y, sr = librosa.load(audio_path, duration=30)
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(2.56, 2.56))
    librosa.display.specshow(S_dB, sr=sr, cmap='magma')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def batch_process(audio_dir="static/audio", output_dir="static/spectrograms"):
    for genre in os.listdir(audio_dir):
        genre_path = os.path.join(audio_dir, genre)
        if not os.path.isdir(genre_path):
            continue

        output_genre_path = os.path.join(output_dir, genre)
        os.makedirs(output_genre_path, exist_ok=True)

        for file in os.listdir(genre_path):
            if not file.endswith(".wav"):
                continue
            input_path = os.path.join(genre_path, file)
            output_path = os.path.join(output_genre_path, file.replace(".wav", ".png"))
            print(f"🎧 Processing: {input_path}")
            generate_spectrogram(input_path, output_path)

if __name__ == "__main__":
    batch_process()
