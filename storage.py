import csv
import os
def save_weather_to_csv(weather_result):
    try:
        file_exists=os.path.exists("weather_history.csv")
        with open("weather_history.csv","r",newline="") as file:
            writer=csv.writer(file)
            if not file_exists:
                writer.writerow(["search_time","city","state","country",
            "temperature","feels_like","condition","humidity","wind_speed"])
            writer.writerow(weather_result)
            print("Weather result saved to weather_history.csv")
            return True
    except(OSError,csv.Error) as error:
        print(error)
        return False

