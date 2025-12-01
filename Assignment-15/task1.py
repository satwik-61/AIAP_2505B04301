# Simple weather fetcher using OpenWeatherMap API
# NOTE: This implementation does not include error handling by request of the user.

import json
import requests
import os
import sys

# Replace the value below with your OpenWeatherMap API key or set the
# environment variable OPENWEATHER_API_KEY before running the script.
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "8e639b78ba113a32ce65284743654ddb")


def get_weather(city: str, api_key: str = API_KEY) -> dict:
	"""Fetch current weather for `city` from OpenWeatherMap and print JSON.

	This function does not use any error handling — it simply performs the
	HTTP request and prints the response JSON.

	Args:
		city: City name (e.g., 'London', 'New York')
		api_key: API key for OpenWeatherMap (default from OPENWEATHER_API_KEY)

	Returns:
		Python dict parsed from the weather API JSON response.
	"""

	url = (
		"http://api.openweathermap.org/data/2.5/weather"
		f"?q={city}&appid={api_key}&units=metric"
	)

	response = requests.get(url)
	data = response.json()

	# Print the JSON output (pretty-printed)
	print(json.dumps(data, indent=2))

	return data


if __name__ == "__main__":
	# If the user passed a city name on the command line, use it. Otherwise
	# prompt for it. This block has no error handling by design.
	if len(sys.argv) > 1:
		city_name = " ".join(sys.argv[1:])
	else:
		city_name = input("Enter city name: ")

	get_weather(city_name)

