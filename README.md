# 🎙️ rsTranslate

> **Your personal AI translator that speaks "Hinglish."**

**rsTranslate** is a full-stack mobile application that bridges the gap between formal English and casual Indian conversation. Unlike robotic translators, it uses Google's Gemini AI to understand context, emotion, and slang (like *"Yaar"* or *"Jugaad"*), delivering voice responses that sound like a real friend.

---

## ✨ Features
* **🗣️ Voice-to-Voice:** Speak in English, hear the response in Hinglish instantly.
* **🧠 Smart AI:** Powered by **Google Gemini 1.5**, allowing for context-aware and humorous translations.
* **☁️ Cloud Native:** The brain of the app (Python backend) is hosted on **Render** (Singapore), making the app lightweight.
* **🌑 Dark Mode:** Features a modern, professional dark UI built with React Native.
* **📱 Production Ready:** Deployed as a standalone Android APK.

---

## 🛠️ Tech Stack

### **Frontend (Mobile App)**
* **Framework:** React Native (via Expo)
* **Language:** TypeScript / JavaScript
* **Key Libraries:** `expo-av` (Audio Recording), `expo-speech` (Text-to-Speech), `axios`

### **Backend (Server)**
* **Framework:** Python (Flask)
* **Hosting:** Render Cloud
* **AI Engine:** Google Gemini API

---

## 📸 Screenshots

---

## 🚀 How It Works
1.  **Record:** The user records a sentence in the mobile app.
2.  **Upload:** The app sends the raw audio to the Python backend on Render.
3.  **Think:** The server sends the audio to Gemini with a custom "Hinglish Persona" prompt.
4.  **Speak:** The translated text is sent back, and the phone speaks it aloud.

---

## 👨‍💻 Author
**Laavanya Dhasmana**
* Full Stack Developer & AI Enthusiast
