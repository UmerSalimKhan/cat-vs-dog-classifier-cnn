from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = load_model('models/cat_dog_classifier_model.h5')

def prepare_image(image_path):
    image = load_img(image_path, target_size=(256, 256))  # Change target_size to match your model's input shape
    image = img_to_array(image)  # Convert to array
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image file provided", 400

    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected file", 400

    # Save the image in a static folder
    filepath = os.path.join('static/uploads', image_file.filename)
    image_file.save(filepath)

    # Prepare the image for prediction
    image = prepare_image(filepath)
    prediction = model.predict(image)

    print(f"Prediction: {prediction}")
    predicted_class = "Dog" if prediction[0][0].round() == 1 else "Cat"

    return render_template('index.html', prediction=predicted_class, image_url=filepath)

if __name__ == '__main__':
    app.run(debug=True)
