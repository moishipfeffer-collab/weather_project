import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def get_location(city, country, state=""):
    api_key=os.getenv("openweather_api_key")
    url="http://api.openweathermap.org/geo/1.0/direct"
    params={"q":[city,state,country],"appid":api_key}
    try:
        response=requests.get(url,params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        if response.status_code==401:
            print("Invalid API key.")
        else:
            print(f"HTTP failed with status code {response.status_code}")
        return None
    except requests.exceptions.RequestException as error:
        print(f"request failed: {error}")
def get_weather(latitude, longitude):
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key=os.getenv("openweather_api_key")
    params={"lat":latitude,"lon":longitude,"appid":api_key,"units":"metric"}
    try:
        response=requests.get(url,params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        if response.status_code==401:
            print("Invalid API key.")
        else:
            print(f"HTTP failed with status code {response.status_code}")
        return None
    except requests.exceptions.RequestException as error:
        print(f"request failed: {error}")
        return None
def get_state(lokation):
    us_state=lokation[0]["state"]
    return us_state
