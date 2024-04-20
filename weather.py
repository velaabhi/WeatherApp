from dotenv import load_dotenv  #for env variables
from pprint import pprint       #for prettyprint
import requests
import os


load_dotenv()

def get_current_weather(city="Pune"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get Weather Conditions ***\n")

    city = input("\nPlease enter a city name ")

    weather_data = get_current_weather(city)

    print()
    pprint(weather_data)