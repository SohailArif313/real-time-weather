# Weather on the Terminal

I wanted a quick way to check the weather without opening a browser, so I built this small command-line application in Python. It fetches real-time weather data from WeatherAPI and displays it directly in the terminal.

The main goal of this project was to practice working with REST APIs, handling JSON responses, and storing API keys securely using environment variables instead of hardcoding them.

---

## Features

- Get the current weather for any city.
- View temperature, weather condition, humidity, and wind speed.
- Store the API key securely with a `.env` file.
- Basic error handling for invalid city names and API requests.

---

## Tech Stack

- **Python**
- **requests**
- **python-dotenv**
- **WeatherAPI**

---

## Installation

**Clone the repository**:

```bash
git clone https://github.com/SohailArif313/real-time-weather.git
```

**Move into the project directory:**

```bash
cd real-time-weather
```