from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------------ FUNCTIONS ------------------

def get_gemini_response(model_name, input_text, image, prompt):
    """Generate response using selected Gemini model"""
    model = genai.GenerativeModel(model_name)
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    """Prepare image for Gemini API input"""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ------------------ STREAMLIT APP ------------------

st.set_page_config(page_title="Gemini Image Demo")
st.header("🧠 Gemini Multi-Doc Q&A Chatbot")

# Model selection
model_choice = st.selectbox(
    "Choose a Gemini model:",
    [
        "gemini-2.5-pro",
        "gemini-2.5-flash",
    ],
    index=0
)

# Text input
input_text = st.text_input("Ask something about the image:", key="input")

# Image upload
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button
submit = st.button("Generate Response")

# Instruction prompt
input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices and answer questions based on the input image.
"""

# Generate response
if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(model_choice, input_text, image_data, input_prompt)
        st.subheader("🧾 The Response:")
        st.write(response)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
