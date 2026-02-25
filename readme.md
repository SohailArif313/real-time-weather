# 🌦 Weather on the Terminal

I got tired of opening a browser just to check if I needed a jacket, so I built this simple Python CLI tool. It’s a straightforward app that pulls live data from WeatherAPI and dumps it right into your terminal. 

I mainly put this together to get better at handling JSON responses and—more importantly—to practice keeping sensitive info like API keys out of my code using environment variables.

---

## 🚀 What it does

- **Instant Weather:** Just type a city name and get the current stats.
- **The Essentials:** Shows temperature (°C), general vibes (condition), humidity, and wind speed.
- **Secure:** Uses `.env` so you don't accidentally leak your API key to GitHub.
- **Fail-safe:** Added some basic error handling so it doesn't just crash if you mistype a city.

---

## 🛠 The Setup

* **Language:** Python 3
* **Libraries:** `requests` (for the API calls) & `python-dotenv` (for the secrets)
* **Data Source:** WeatherAPI

---

## ⚙ How to get it running

1. **Grab the code**
   ```bash
   git clone [https://github.com/yourusername/weather-cli-app.git](https://github.com/yourusername/weather-cli-app.git)
   cd weather-cli-app