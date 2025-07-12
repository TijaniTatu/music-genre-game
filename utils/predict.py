from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os

model = load_model("model/cnn_genre_classifier.keras")
genre_labels = sorted(os.listdir("static/spectrograms"))

def predict_genre(image_path):
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return genre_labels[np.argmax(prediction)]
