# Siri Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> **Siri** is a Python-based voice assistant that responds to your voice commands, fetches news and weather, tells jokes, plays music, and answers general queries using AI. It features both a command-line and a modern Tkinter GUI interface.

---

## 🚀 Features
- **Voice Activation:** Listens for the wake word ("hey siri") and processes further commands.
- **Web Actions:** Opens popular websites like Google, YouTube, Facebook, and Instagram.
- **Jokes:** Tells jokes using the `pyjokes` library.
- **News Headlines:** Fetches and reads out the latest news headlines.
- **Weather Updates:** Provides current weather information and air quality.
- **Music Playback:** Plays music from a predefined library or Spotify.
- **AI Chat:** Handles general queries using OpenAI's API via OpenRouter.
- **Interruptible Speech:** Allows you to interrupt the assistant while it is speaking.


---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/siri-voice-assistant.git
   cd siri-voice-assistant
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   Create an `env.py` file in the project root with your API keys and URLs. Example:
   ```python
   API_KEY = {
       "NEWS_API": "<your-news-api-key>",
       "OPEN_ROUTER_API": "<your-openrouter-api-key>",
       "WEATHER_API": "<your-weather-api-key>",
   }

   URL = {
       "NEWS_URL": f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY['NEWS_API']}",
       "OPEN_ROUTER_BASE_URL": "https://openrouter.ai/api/v1",
       "SPOTIFY_URL": "<your-spotify-url>",
       "WEATHER_URL": f"http://api.weatherapi.com/v1/current.json?key={API_KEY['WEATHER_API']}&q=New Delhi&aqi=yes"
   }

   MODEL = {
       "OPEN_ROUTER_MODEL": "mistralai/mistral-7b-instruct",
   }
   ```
   > **Note:** `env.py` is in `.gitignore` to protect your keys.

---

## 🖥️ Usage

### Command-Line Interface
```bash
python main.py
```
- Say "hey siri" to activate, then speak your command.
- Say "exit" to quit.

## 🛠️ Customization
- **Music Library:** Edit `musicLibrary.py` to add or change music links.
- **Commands:** Extend `processCommand` in `main.py` to add new features.

---

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits
- [OpenAI](https://openai.com/) for language models
- [NewsAPI](https://newsapi.org/) for news headlines
- [WeatherAPI](https://www.weatherapi.com/) for weather data
- [gTTS](https://pypi.org/project/gTTS/) for text-to-speech
- [pyjokes](https://pypi.org/project/pyjokes/) for jokes

---

> **Disclaimer:** This project is for educational purposes. Do not share your API keys publicly. 