from __future__ import annotations
import json
import os
from typing import Any, Dict, Optional
from task2 import get_weather_with_handling
from task3 import extract_weather_fields, display_weather_summary
def _extract_and_prepare_record(api_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Return a compact record dict with numeric temp/humidity and description."""
    fields = extract_weather_fields(api_payload)
    # Convert temperature '18°C' -> 18 (int) when possible
    temp_raw = fields.get("temperature")
    temp_val = None
    if isinstance(temp_raw, str) and temp_raw.endswith("°C"):
        try:
            temp_val = int(temp_raw.rstrip("°C"))
        except Exception:
            # best-effort – try float then round
            try:
                temp_val = round(float(temp_raw.rstrip("°C")))
            except Exception:
                temp_val = None
    # Convert humidity '60%' -> 60
    humidity_raw = fields.get("humidity")
    humidity_val = None
    if isinstance(humidity_raw, str) and humidity_raw.endswith("%"):
        try:
            humidity_val = int(humidity_raw.rstrip("%"))
        except Exception:
            humidity_val = None

    return {
        "city": fields.get("city") or api_payload.get("name") or "",
        "temp": temp_val,
        "humidity": humidity_val,
        "weather": fields.get("description") or "",
    }

def get_display_and_store_weather(city: str, api_key: Optional[str] = None, filename: str = "results.json") -> Optional[Dict[str, Any]]:
    if api_key is None:
        api_key = os.environ.get("OPENWEATHER_API_KEY")
    if api_key is None:
        API_KEY = "8e639b78ba113a32ce65284743654ddb"
        api_key = API_KEY
    result = get_weather_with_handling(city, api_key=api_key)
    # Handle errors returned by get_weather_with_handling
    if isinstance(result, dict) and result.get("error"):
        status_code = result.get("status_code")
        body = result.get("body")
        # detect city not found
        if status_code == 404 or (isinstance(body, dict) and "city" in str(body.get("message", "")).lower() and "not" in str(body.get("message", "")).lower()):
            print("Error: City not found. Please enter a valid city.")
            return None
        # Other errors — print the error dict and return
        print(json.dumps(result, indent=2))
        return None
    # Success path — prepare a compact record, display and append it
    record = _extract_and_prepare_record(result)
    # Print the user-friendly summary
    display_weather_summary(result)
    # Also print the compact JSON record for clarity
    print("\nJSON output:")
    print(json.dumps(record, indent=2, ensure_ascii=False))
    # Append to file: read existing array or start a new one
    stored = []
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as fh:
                stored = json.load(fh)
                if not isinstance(stored, list):
                    stored = []
        except Exception:
            # if file exists but is not readable/valid, overwrite with new list
            stored = []
    stored.append(record)
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(stored, fh, indent=2, ensure_ascii=False)
    return record
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # treat first argument(s) as city and optional second argument as api key
        if len(sys.argv) > 2:
            # city may be multi-word, consume all args except last as city
            city_name = " ".join(sys.argv[1:-1])
            api_key_arg = sys.argv[-1]
            get_display_and_store_weather(city_name, api_key=api_key_arg)
            sys.exit(0)
        else:
            city_name = " ".join(sys.argv[1:])
    else:
        city_name = input("Enter city name: ")

    # default behavior: rely on precedence inside get_display_and_store_weather
    # (explicit CLI arg > OPENWEATHER_API_KEY env var > API_KEY constant in file)
    get_display_and_store_weather(city_name)
