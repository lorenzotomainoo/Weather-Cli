import requests
import os
from dotenv import load_dotenv
import sys
import argparse
import time
import json

CACHE_DIR = "cache"

def get_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API key not found. Please check your .env file.", file=sys.stderr)
        sys.exit(1)
    return api_key

def fetch_weather_data(city, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}"

    cache_data = read_cache(city)
    if cache_data:
        return cache_data

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json() 
        save_cache(city, data)
        return data
        
    except requests.exceptions.RequestException:
        print("Error: Connection failed or city not found. Please check the city name.", file=sys.stderr)
        return None
    
def show_current_weather(weather_data, city):
    try:
        current = weather_data['currentConditions']
        print(f"\n{'='*30}")
        print(f" CURRENT WEATHER: {city.upper()}")
        print(f"{'='*30}")
        print(f"Temperature:  {current['temp']} °C")
        print(f"Humidity:     {current['humidity']}%")
        print(f"Wind Speed:   {current['windspeed']} km/h")
        print(f"Conditions:   {current['conditions']}")
    except KeyError:
        print("Error: Unable to read current weather data from the JSON response.", file=sys.stderr)

def show_forecast(weather_data, days):
    try:
        forecast = weather_data['days']
        print(f"\n--- Forecast for the next {days} days ---")

        for i in range(1, days + 1):
            day = forecast[i]
            date = day['datetime']
            temp_max = day['tempmax']
            temp_min = day['tempmin']
            conditions = day['conditions']
            
            print(f"[{date}] {conditions} - High: {temp_max}°C | Low: {temp_min}°C")
    except (KeyError, IndexError):
        print("Error: Unable to generate the weather forecast.", file=sys.stderr)

def get_location_from_ip():
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == "success":
            return data['city']
        else:
            return None
    except requests.exceptions.RequestException:
        print("Error: Connection failed while trying to determine location via IP.", file=sys.stderr)
        return None
    
def read_cache(city):
    filename = os.path.join(CACHE_DIR, f".cache_{city.lower()}.json")
    
    if os.path.exists(filename):
        age = time.time() - os.path.getmtime(filename)
        if age < 1800: 
            with open(filename, "r") as file:
                return json.load(file)
    return None

def save_cache(city, weather_data):
    os.makedirs(CACHE_DIR, exist_ok=True)
    filename = os.path.join(CACHE_DIR, f".cache_{city.lower()}.json")
    
    with open(filename, "w") as file:
        json.dump(weather_data, file)

def main():
    api_key = get_api_key()
    
    parser = argparse.ArgumentParser(description="Weather CLI: Get current weather and forecasts.")
    parser.add_argument("-c","--city", type=str, required=False, help="City name, in english | (leave empty to use your current IP location).")
    parser.add_argument("-d","--day", type=int, required=False, default=3, help="Number of days of forecast data")

    args = parser.parse_args()
    city = args.city

    if not city:
        city = get_location_from_ip()
        if not city:
            print("Error: Location not found. Please provide a city manually using --city.", file=sys.stderr)
            sys.exit(1)

    weather_data = fetch_weather_data(city, api_key)
    
    if weather_data:
        show_current_weather(weather_data, city)
        show_forecast(weather_data, args.day)

if __name__ == "__main__":
    main()