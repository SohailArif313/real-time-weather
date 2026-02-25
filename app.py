import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(key_name):
    try:
        key = os.getenv(key_name)
        if key:
            print(f"{key_name} successfully loaded")
            return key
        else:
            raise ValueError(f"{key_name} not found in environment variables")
    except Exception as error:
        print(f"Something went wrong while loading {key_name}: {error}")
        return None


API_KEY = get_api_key("API_KEY")

if not API_KEY:
    exit()

city = input("Enter city: ")

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"

try:
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("❌ Error:", data["error"]["message"])
    else:
        print(f"\n📍 {data['location']['name']}, {data['location']['country']}")
        print(f"🌡 Temperature: {data['current']['temp_c']}°C")
        print(f"☁ Condition: {data['current']['condition']['text']}")
        print(f"🌬 Wind: {data['current']['wind_kph']} kph")
        print(f"💧 Humidity: {data['current']['humidity']}%")

except Exception as e:
    print("Something went wrong:", e)