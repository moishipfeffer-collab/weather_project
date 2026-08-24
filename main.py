from inputs_and_validation import *
from http_requests import *
from proses_print import *
from storage import *
import requests
def main():
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
    if not weather_data:
        return
    csv_weather=to_csv(weather_data)
    print_weather(weather_data)    
    save_weather_to_csv(csv_weather)

main()
