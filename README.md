# Weather Project

A Python project that gets current weather information for a city using the OpenWeather API, validates user input, handles API and CSV errors, and saves successful weather searches to a CSV history file.

## Features

* Ask the user for a city name and country code.
* Support state codes when needed.
* Find the latitude and longitude of a location using the OpenWeather Geocoding API.
* Get current weather information using the OpenWeather API.
* Display:

  * City
  * State
  * Country
  * Temperature
  * Feels-like temperature
  * Weather condition
  * Humidity
  * Wind speed
* Save weather results to `weather_history.csv`.
* Add the CSV header only when the file is created for the first time.
* Handle invalid input.
* Handle invalid API keys.
* Handle unsuccessful HTTP responses.
* Handle unexpected API response data.
* Handle CSV/file-writing errors without crashing the entire program.

## Technologies

* Python
* `requests`
* `python-dotenv`
* `csv`
* OpenWeather API

## Project Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install requests python-dotenv
```

## Environment Variables

Create a `.env` file in the project folder:

```text
openweather_api_key=YOUR_API_KEY
```

Do not upload the `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
.venv/
```

## Running the Project

Run:

```bash
python weather.py
```

The program will ask for location information, retrieve the weather, display it, and try to save the result to:

```text
weather_history.csv
```

## CSV Format

The CSV file contains:

```text
search_time,city,state,country,temperature,feels_like,condition,humidity,wind_speed
```

Each successful search is added as a new row.

## Error Handling

The program is designed not to crash when possible.

Examples include:

* Empty or invalid location input.
* Invalid API key.
* HTTP request failures.
* Missing or unexpected values in the API response.
* Empty API result lists.
* Problems opening or writing to the CSV file.

If the weather was received but could not be saved, the weather information is still displayed.

When saving succeeds:

```text
Weather result saved to weather_history.csv
```

If saving fails, the relevant CSV/file error is displayed.

## API

This project uses the OpenWeather API for:

* Geocoding a city into latitude and longitude.
* Retrieving current weather information.

The API key is loaded from `.env` instead of being written directly in the source code.
