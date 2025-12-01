from __future__ import annotations
from typing import Optional
from task2 import get_weather_with_handling
from task3 import display_weather_summary
API_KEY = "8e639b78ba113a32ce65284743654ddb"
def get_and_display_weather(city: str, api_key: Optional[str] = None) -> None:
    if api_key is None:
        api_key = API_KEY
    result = get_weather_with_handling(city, api_key=api_key)
    # The helper returns an error dict with `error` if something went wrong.
    if isinstance(result, dict) and result.get("error"):
        # Handle the specific case where the API indicates city not found.
        status_code = result.get("status_code")
        body = result.get("body")
        # Detect OpenWeatherMap's typical 404/cod message
        body_message = None
        if isinstance(body, dict):
            body_message = str(body.get("message") or body.get("cod") or "")
        if status_code == 404 or (body_message and "city" in body_message.lower() and "not" in body_message.lower()):
            print("Error: City not found. Please enter a valid city.")
            return
        # otherwise print the error object (already structured)
        print(result)
        return
    # Success path: `result` is the API payload. Show a friendly summary.
    display_weather_summary(result)
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:])
        if len(sys.argv) > 2:
            api_key_arg = sys.argv[2]
            get_and_display_weather(city_name, api_key=api_key_arg)
            sys.exit(0)
    else:
        city_name = input("Enter city name: ")
    get_and_display_weather(city_name)
