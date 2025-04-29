import streamlit as st
import os
import cv2
import numpy as np
import base64
import requests
from PIL import Image
from dotenv import load_dotenv  # ✅ Added

# Load environment variables from .env file
load_dotenv()

# Streamlit config
st.set_page_config(page_title="Celebrity Recognition", layout="centered")

# Create upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Groq API Key securely from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def detect_faces(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Load the pre-trained Haar Cascade model for detecting frontal faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    #Detect faces in the grayscale image
    # 1.1 = scale down image by 10% each time, 5 = at least 5 neighbor rectangles to confirm a face
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) == 0:
        return None, img_rgb

    largest_face = max(faces, key=lambda r: r[2] * r[3]) # to find area multiply width and height
    return [largest_face], img_rgb

def draw_faces(image, faces, player_name):
    for (x, y, w, h) in faces:
        
        # Draw a green rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        font_scale = 1
        cv2.putText(image, player_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2)
    return image

def get_info(image_path):
    with open(image_path, "rb") as img_file:
        # Base64 Encoding: Converts binary data (like an image) into text
        # which can be sent through protocols that support only text.
        img_base64 = base64.b64encode(img_file.read()).decode()

    headers = {
        # The Bearer token allows the server to verify that the request is coming 
        "Authorization": f"Bearer {GROQ_API_KEY}",
        # Specifies that the request content is JSON
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """You are an expert AI trained in recognizing Bollywood Actresses with high accuracy. 
Carefully analyze the given image and identify the Actress with certainty. 
If a well-known Actress is present, return the following details in a structured format:

- **Full Name**: (Only the Actress full name, no extra text)
- **Nationality**: (Country of origin)
- **Movies**: (Notable Movies, max 2-3)

If multiple Actresses are detected, return only the **most famous one**.
If no Actress is recognized, respond with "Unknown".
"""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_base64}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1024
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Unknown"

# === Streamlit UI ===
st.title("👗 Guess The Actress ?")

uploaded_file = st.file_uploader("Upload a Actress's image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    faces, img_rgb = detect_faces(image_path)

    if faces:
        with st.spinner("Recognizing Actress..."):
            Actress_info = get_info(image_path)
        st.subheader("🎯 Identified Actress Info")
        col1 , col2 = st.columns(2)
        with col1:
            st.markdown(Actress_info)

        name = Actress_info.split("\n")[0].replace("**Full Name**: ", "").strip()
        result_img = draw_faces(img_rgb.copy(), faces, name)
        with col2:
            st.image(result_img, caption="Detected Face", use_container_width =True)

        result_img_path = os.path.join(UPLOAD_FOLDER, f"result_{uploaded_file.name}")
        cv2.imwrite(result_img_path, cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))

    else:
        st.warning("No face detected. Try another image.")
