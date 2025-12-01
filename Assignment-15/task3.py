from __future__ import annotations
import sys
from typing import Any, Dict, Optional
def extract_weather_fields(api_response: Dict[str, Any]) -> Dict[str, Optional[str]]:
	# City name
	city = api_response.get("name") if isinstance(api_response, dict) else None
	# Temperature and humidity live under `main` normally
	main = api_response.get("main") if isinstance(api_response, dict) else None
	temp = None
	humidity = None
	if isinstance(main, dict):
		if "temp" in main and main["temp"] is not None:
			# round to nearest integer for display
			try:
				temp = f"{round(float(main['temp']))}°C"
			except Exception:
				temp = str(main.get("temp"))
		if "humidity" in main and main["humidity"] is not None:
			try:
				humidity = f"{int(main['humidity'])}%"
			except Exception:
				humidity = str(main.get("humidity"))
	# Weather description usually comes from `weather` list
	description = None
	weather_list = api_response.get("weather") if isinstance(api_response, dict) else None
	if isinstance(weather_list, list) and len(weather_list) > 0 and isinstance(weather_list[0], dict):
		desc = weather_list[0].get("description")
		if isinstance(desc, str):
			# Title-case for nicer display (e.g. "clear sky" -> "Clear Sky")
			description = desc.title()

	return {
		"city": city,
		"temperature": temp,
		"humidity": humidity,
		"description": description,
	}

def display_weather_summary(api_response: Dict[str, Any]) -> None:
	fields = extract_weather_fields(api_response)
	city = fields.get("city") or "N/A"
	temp = fields.get("temperature") or "N/A"
	hum = fields.get("humidity") or "N/A"
	desc = fields.get("description") or "N/A"

	print(f"City: {city}")
	print(f"Temperature: {temp}")
	print(f"Humidity: {hum}")
	print(f"Weather: {desc}")

if __name__ == "__main__":
	# Simple demo: accept a JSON payload from stdin or use a tiny sample if no
	# data is provided. This keeps the file self-contained for quick demos.
	import json
	if not sys.stdin.isatty():
		# read JSON from stdin
		payload = json.load(sys.stdin)
		display_weather_summary(payload)
	else:
		# Show a small example
		sample = {
			"name": "London",
			"main": {"temp": 18.3, "humidity": 60},
			"weather": [{"description": "clear sky"}],
		}
		display_weather_summary(sample)

