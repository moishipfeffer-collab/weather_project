from datetime import datetime
def process_weather_data(location, weather,state=""):
    time=datetime.now()
    try:
        city=location[0]["name"]
        country=location[0]["country"]
        temp=weather["main"]["temp"]
        feels_like=weather["main"]["feels_like"]
        humidity=weather["main"]["humidity"]
        description=weather["weather"][0]["description"]
        speed=weather["wind"]["speed"]
        if not isinstance(city,str):
            raise TypeError
        if not isinstance(temp,(int,float)):
            raise TypeError
        if not isinstance(feels_like,(int,float)):
            raise TypeError
        if not isinstance(humidity,(int,float)):
            raise TypeError
        if not isinstance(description,str):
            raise TypeError
        if not isinstance(speed,(int,float)):
            raise TypeError
        weather_data={"search_time":str(time),"city":city,"state":state,
        "country":country,"temperature":temp,"feels_like":feels_like,
        "condition":description,"humidity":humidity,"wind_speed":speed}
        return weather_data
    except(KeyError,IndexError,TypeError):
        print("The API response did not contain the expected data.")
        return None
def to_csv(weather_data):
    return[weather_data["search_time"],weather_data["city"],
    weather_data["state"],weather_data["country"],
    weather_data["temperature"],weather_data["feels_like"],
    weather_data["condition"],weather_data["humidity"],weather_data["wind_speed"]]
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
