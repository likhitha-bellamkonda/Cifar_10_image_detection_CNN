import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load CNN model
model = load_model("cnn_model.h5")

# CIFAR-10 class names
classes = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]

st.title("CIFAR-10 CNN Image Classification")
st.write("""
Please upload images related to:
Airplane, Automobile, Bird, Cat, Deer,
Dog, Frog, Horse, Ship, or Truck.
""")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image and convert to RGB
    image = Image.open(uploaded_file).convert("RGB")

    # Show uploaded image
    st.image(image, caption="Uploaded Image", width=250)

    # Resize image to CIFAR-10 size
    image = image.resize((32, 32))

    # Convert image to numpy array
    img_array = np.array(image)

    # Normalize pixel values
    img_array = img_array / 255.0

    # CNN expects shape: (1, 32, 32, 3)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    st.success(f"Predicted Class: {classes[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}")