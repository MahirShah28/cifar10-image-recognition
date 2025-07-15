# CIFAR-10 Image Recognition with CNN

This project demonstrates image classification on the CIFAR-10 dataset using a Convolutional Neural Network (CNN) built with TensorFlow/Keras. A Streamlit web app is included for live prediction — users can upload an image and receive a real-time classification.

## Dataset

- CIFAR-10: 60,000 color images (32x32 pixels)
- Classes:
  - airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

## Features

- Custom CNN trained on CIFAR-10 dataset
- Achieved 77.9% test accuracy
- Model saved and reloaded using JSON and H5 files
- Supports external image predictions (PNG, JPG)
- Streamlit interface for real-time classification

## Folder Structure
cifar10-image-recognition/
├── app.py
├── model_structure.json
├── model_weight.weights.h5
├── airplane.png
├── dog.png
├── ship.png
├── README.md

## How to Run the App

1. Clone this repository:

git clone https://github.com/MahirShah28/cifar10-image-recognition.git
cd cifar10-image-recognition

2. Install dependencies:
   pip install streamlit tensorflow pillow numpy
   
3. Run the Streamlit app:
   streamlit run app.py

Author
Your Name: Mahir Shah
Email: mahirshah2815@gmail.com






