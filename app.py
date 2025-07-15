import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.utils import img_to_array


# Load CIFAR-10 class labels
class_labels = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

# Load model
with open("model_structure.json", "r") as f:
    model = model_from_json(f.read())
model.load_weights("model_weight.weights.h5")

# UI
st.title("🚀 CIFAR-10 Image Classifier")
st.markdown("Upload a 32x32 image (e.g. dog.png, ship.png) and the model will predict the class.")

uploaded_file = st.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=150)

    image_resized = image.resize((32, 32))
    img_array = img_to_array(image_resized)
    img_batch = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_batch)
    index = np.argmax(prediction[0])
    confidence = prediction[0][index]
    label = class_labels[index]

    st.success(f"✅ Predicted Class: **{label}**")
    st.info(f"📈 Confidence: {confidence:.2f}")
