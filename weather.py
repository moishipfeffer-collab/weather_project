import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
def get_city():
    city=input("enter a city: ")
    return city.strip()
def check_city(city):
    return city != ""
def raise_city_error():
    raise ValueError("the input must not be empty")
def raise_code_error():
    raise ValueError("code must contains exactly two letters")
def get_country_code():
    country_code=input("enter country code: ")
    return country_code.upper().strip()
def check_cod(country_code):
    return len(country_code) == 2
def check_us(country_code):
    return country_code == "US"
def get_state_code():
    state_code=input("enter state code: ")
    return state_code.upper().strip()
def get_location(city, country, state=""):
    api_key=os.getenv("openweather_api_key")
    url="http://api.openweathermap.org/geo/1.0/direct"
    params={"q":[city,state,country],"appid":api_key}
    resoonse=requests.get(url,params=params)
    if resoonse.status_code!=200:
        return None
    return resoonse.json()
def get_weather(latitude, longitude):
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key=os.getenv("openweather_api_key")
    params={"lat":latitude,"lon":longitude,"appid":api_key,"units":"metric"}
    resoonse=requests.get(url,params=params)
    if resoonse.status_code!=200:
        return None
    return resoonse.json()
def get_state(lokation):
    us_state=lokation[0]["state"]
    return us_state
def process_weather_data(location, weather,state=""):
    time=datetime.now()
    city=location[0]["name"]
    country=location[0]["country"]
    temp=weather["main"]["temp"]
    feels_like=weather["main"]["feels_like"]
    humidity=weather["main"]["humidity"]
    description=weather["weather"][0]["description"]
    speed=weather["wind"]["speed"]
    weather_data={"search_time":str(time),"city":city,"state":state,
    "country":country,"temperature":temp,"feels_like":feels_like,
    "condition":description,"humidity":humidity,"wind_speed":speed}
    return weather_data
def print_weather(weather_result):
    city=weather_result["city"]
    country=weather_result["country"]
    temp=weather_result["temperature"]
    feels_like=weather_result["feels_like"]
    condition=weather_result["condition"]
    humidity=weather_result["humidity"]
    wind_speed=weather_result["wind_speed"]
    print(f"City: {city}\nCountry: {country}\nTemperature: {temp}C\nFeels_like: {feels_like}C\nCondition: {condition}\nHumidity: {humidity}%\nWind speed: {wind_speed}m/s")
    if weather_result["state"]!="":
        print(f"State/Region:{weather_result["state"]}")        


def run():
    city=get_city()
    if not check_city(city):
        raise_city_error()
    country=get_country_code()
    if not check_cod(country):
        raise_code_error()
    us= check_us(country)
    if us:
        state=get_state_code()
        if not check_cod(state):
            raise_code_error()
        location=get_location(city,country,state)
    else:
        location=get_location(city,country)
    if not location:
        print("Location not found")
        return
    lat=location[0]["lat"]
    lon=location[0]["lon"]
    weather=(get_weather(lat,lon))
    if us:
        weather_data=process_weather_data(location,weather,get_state(location))
    else:
        weather_data=process_weather_data(location,weather)
    print_weather(weather_data)    

run()
