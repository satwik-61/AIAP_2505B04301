"""Robust weather fetcher with error handling.
This module provides `get_weather_with_handling` which calls the OpenWeatherMap
current weather API and prints the response as JSON. The function handles
common failure modes and always prints a JSON object describing the result
(either the successful payload or an error object).

Usage:
  - Set OPENWEATHER_API_KEY environment variable, or supply api_key argument.
  - Call get_weather_with_handling("City Name")

Note: This file intentionally includes error handling, unlike `task1.py`.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict, Optional

import requests


DEFAULT_API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def _print_json(obj: Any) -> None:
	"""Helper: pretty-print JSON to stdout."""

	print(json.dumps(obj, indent=2, ensure_ascii=False))


def get_weather_with_handling(city: str, api_key: Optional[str] = DEFAULT_API_KEY) -> Dict[str, Any]:
	"""Fetch current weather for `city` and print JSON output with robust error handling.

	This function will always print a JSON object. On success the object is the
	weather payload returned by the API. On failure, the object will contain an
	`error` key and additional context describing what went wrong.
	Args:
		city: City name (e.g., "London", "New York")
		api_key: API key for OpenWeatherMap (defaults to OPENWEATHER_API_KEY env var)

	Returns:
		The parsed JSON object (on success) or an error object (on failure).
	"""

	if not api_key:
		error_obj = {"error": "missing_api_key", "message": "No OpenWeatherMap API key provided."}
		_print_json(error_obj)
		return error_obj

	# Build request
	url = (
		"http://api.openweathermap.org/data/2.5/weather"
		f"?q={city}&appid={api_key}&units=metric"
	)

	try:
		response = requests.get(url, timeout=10)
	except requests.exceptions.RequestException as exc:
		# Network-level / connection errors
		error_obj = {"error": "request_exception", "message": str(exc)}
		_print_json(error_obj)
		return error_obj

	# HTTP-level errors (non-200)
	if response.status_code != 200:
		# Attempt to parse error body
		try:
			body = response.json()
		except ValueError:
			body = {"raw_text": response.text}

		error_obj = {
			"error": "http_error",
			"status_code": response.status_code,
			"body": body,
		}
		_print_json(error_obj)
		return error_obj

	# Try to parse JSON
	try:
		data = response.json()
	except ValueError as exc:
		error_obj = {"error": "invalid_json", "message": str(exc), "text": response.text}
		_print_json(error_obj)
		return error_obj

	# Success
	_print_json(data)
	return data


if __name__ == "__main__":
	# CLI entry point
	if len(sys.argv) > 1:
		city_name = " ".join(sys.argv[1:])
	else:
		city_name = input("Enter city name: ").strip()

	# Allow overriding the API key from environment or by using the environment
	# variable directly. For one-off quick runs, you can set the OPENWEATHER_API_KEY
	# env var before running the script.
	get_weather_with_handling(city_name)

