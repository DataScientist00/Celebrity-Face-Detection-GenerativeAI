# 🎥 Celebrity Recognition – Bollywood Actress Identifier

## Watch the Demo 📺
[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube&logoColor=white&style=for-the-badge)](https://youtu.be/EZM5AzfyXUU)

This project is a **Streamlit-based web application** that uses computer vision and AI to detect and identify **Bollywood actresses** from uploaded images. It utilizes **OpenCV** for face detection and the **Groq API with LLaMA models** for intelligent identification.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue" />
  <img src="https://img.shields.io/badge/Streamlit-App-orange" />
  <img src="https://img.shields.io/badge/OpenCV-FaceDetection-green" />
</div>

---

![Image](https://github.com/user-attachments/assets/a0fe9451-f2df-4aab-800d-155eea6d66c7)

## 🧠 Features

- 📸 Upload an image containing a Bollywood actress.
- 🤖 Automatically detect the most prominent face using Haar Cascades.
- 🧾 Use **Groq's LLaMA 4 model** to recognize the actress and return:
  - Full Name
  - Nationality
  - Notable Movies
- ✅ Display the results along with the marked image.

---

## 📁 Project Structure

```
├── app.py                         # Main Streamlit application
├── .env                           # Environment variables (Groq API key)
├── haarcascade_frontalface_default.xml  # Haar Cascade for face detection
├── requirements.txt               # Python dependencies
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/DataScientist00/Celebrity-Face-Detection-GenerativeAI.git
cd Celebrity-Face-Detection-GenerativeAI
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up the `.env` file**

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## 📷 Sample Output

When an image is uploaded, the app detects the face and overlays the identified actress's name. The info panel displays structured results like:

Example - 

![Image](https://github.com/user-attachments/assets/fe5e3f5a-44ab-466c-850f-304bdabdcfb1)

```
**Full Name**: Alia Bhatt  
**Nationality**: Indian  
**Movies**: Gully Boy , Raazi , Highway
```

---

## 🛠️ Technologies Used

- Python 3.9+
- Streamlit
- OpenCV
- Groq API (LLaMA 4 model)
- dotenv
- PIL, base64, requests

---

## 📌 Notes

- Only **one face** is analyzed – the largest detected face in the image.
- Designed specifically for **Bollywood actresses**.
- Requires internet connection to query Groq API.

---

## 📞 Contact
For any questions or feedback, reach out to:
- **Email**: nikzmishra@gmail.com
- **YouTube**: [Channel](https://www.youtube.com/@DataScienceSensei/videos)

---

⚡️ Built with love by an anime fan for anime fans.  
Follow the repo and ⭐ it if you found it useful!

