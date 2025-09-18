
---

# 🧠 AI Agent – Voice & GUI Based Assistant

**AI Agent** is a smart assistant combining **speech recognition**, **text-to-speech**, and a **Tkinter-based GUI**. It allows you to interact via voice or text, responds with natural-sounding speech, and can perform useful actions like checking the weather, telling jokes, or launching popular websites and utilities.

---

## 🚀 Features

* 🎤 **Speech Recognition**
  Converts spoken input into text using your microphone (`speech_to_text.py`).

* 🗣 **Text-to-Speech**
  Speaks back responses using a natural voice (`text_to_speech.py`).

* 🌦 **Live Weather Updates**
  Fetches real-time weather from OpenWeatherMap API (`Weather.py`).

* 📺 **Web Shortcuts**
  Opens YouTube, Google, Wikipedia, WhatsApp Web, and more.

* ⏰ **Utilities**
  Tells the current time, opens calculator, plays music, and more.

* 😂 **Fun Mode**
  Responds with jokes and motivational quotes.

* 🖥 **GUI Interface**
  Simple and clean interface using `Tkinter` (`GUI.py`).

---

## 📂 Project Structure

```
AI-Agent/
├── action.py             # Core logic – processes user commands
├── GUI.py                # Tkinter GUI interface
├── speech_to_text.py     # Converts speech to text
├── text_to_speech.py     # Converts text to speech
├── Weather.py            # Fetches weather using OpenWeatherMap API
├── bing_weather.html     # (Optional HTML for scraping fallback)
└── images/
    └── AI AGENT.jpeg     # GUI logo
```

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### ✅ Dependencies

* `speechrecognition`
* `pyttsx3`
* `pyaudio`
* `requests`
* `pillow`
* `pyjokes`

### 3. Setup Weather API

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and add it in `Weather.py`:

```python
api_key = "YOUR_API_KEY_HERE"
```

---

## ▶️ Usage

### Run the GUI Assistant:

```bash
python GUI.py
```

### Run the Voice Assistant in Console:

```bash
python action.py
```

---

## 📸 Screenshots

> 💡 *Add a screenshot of your chatbot GUI here:*

<img width="690" height="886" alt="image" src="https://github.com/user-attachments/assets/16b2171f-0294-4575-a331-25bbd07d9b27" />


---

## 💡 Future Improvements

* Add support for email, news updates, and reminders
* Enhance GUI design with themes and animations
* Add continuous background listening
* Integrate AI-powered conversation engine (e.g., GPT)

---

## 👤 Author

**Prajwal M**
Built as a Python project combining Speech AI + GUI for a fully interactive assistant experience.


