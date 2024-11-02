# Cat vs. Dog Classifier Web App

![Cat vs. Dog Classifier](static/images/cat.jpg)
![Cat vs. Dog Classifier](static/images/dog.jpg)

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Future Work](#future-work)
- [Model Details](#model-details)
- [License](#license)

## Overview
The Cat vs. Dog Classifier is a web application that uses a Convolutional Neural Network (CNN) to classify images as either a cat or a dog. This project aims to provide a user-friendly interface for users to upload images and receive instant predictions based on a trained model.

## Technologies Used
- Python
- Flask
- Keras
- TensorFlow
- OpenCV
- HTML, CSS, JavaScript
- Bootstrap
- Git & GitHub

## Features
- User can upload images of cats or dogs.
- The model classifies the uploaded image as either "Cat" or "Dog."
- Displays the prediction result along with the uploaded image.
- Responsive design using Bootstrap.

## Setup Instructions
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UmerSalimKhan/cat-vs-dog-classifier-cnn.git
   cd cat-vs-dog-classifier-cnn
   ```

2. **Install dependencies**
   Install the libraries in Requirement.txt
   ```bash
   pip install -r requirements.txt"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## Future Work
1. The accuracy of the model is around 88% but the model is showing some poor performance with cat images.
2. The file.txt is a bit outdated. It contain those files which are likely needed. (Extra Info)
3. Hosting the application.

## Model Details
#### Summary
![Model Summary](static/Outputs/Model%20Summary.png)

#### Accuracy
![Model Accuracy](static/Outputs/Model%20Accuracy.png)

#### Loss
![Model Loss](static/Outputs/Model%20Loss.png)

## License 
### How to Customize:
- **Project Title and Description:** Make sure to replace the title and description with your specific project details.
- **Image:** Replace the image link with one from your project or remove it if you don't have a relevant image.
- **Dependencies:** Update the list of dependencies based on your actual project requirements.
- **Instructions:** Ensure that all the setup instructions are correct and reflect the steps needed to get your project running.
- **Contributing:** Modify the contributing section if you have specific guidelines for contributions.
