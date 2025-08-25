import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Plant Disease Detection", page_icon="🌱", layout="centered")

# Title
st.title("🌱 Plant Disease Detection")
st.write("Upload a leaf image and let the AI detect if it's healthy or diseased!")

# Upload image
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    st.write("🔍 Analyzing...")

    # ⚠️ TODO: Replace with your trained model later
    # Example: model = tf.keras.models.load_model("plant_model.h5")
    classes = ["Healthy 🌿", "Diseased 🍂"]
    prediction = np.random.choice(classes)

    # Show result
    st.success(f"Prediction: **{prediction}**")
