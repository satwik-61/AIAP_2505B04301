import io
import sys
import unittest
from unittest import mock

from task4 import get_and_display_weather


class TestTask4(unittest.TestCase):
    def capture_print(self, func, *args, **kwargs):
        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            func(*args, **kwargs)
            return buf.getvalue()
        finally:
            sys.stdout = old_stdout

    def test_valid_city_shows_summary(self):
        payload = {
            "name": "New York",
            "main": {"temp": 22.4, "humidity": 55},
            "weather": [{"description": "few clouds"}],
        }

        with mock.patch("task4.get_weather_with_handling", return_value=payload):
            printed = self.capture_print(get_and_display_weather, "New York")
            self.assertIn("City: New York", printed)
            self.assertIn("Temperature: 22°C", printed)
            self.assertIn("Humidity: 55%", printed)
            self.assertIn("Weather: Few Clouds", printed)

    def test_invalid_city_404(self):
        error = {"error": "http_error", "status_code": 404, "body": {"message": "city not found"}}

        with mock.patch("task4.get_weather_with_handling", return_value=error):
            printed = self.capture_print(get_and_display_weather, "xyz123")
            self.assertIn("Error: City not found. Please enter a valid city.", printed)

    def test_invalid_city_message_text(self):
        error = {"error": "http_error", "status_code": 400, "body": {"message": "City not found in database"}}

        with mock.patch("task4.get_weather_with_handling", return_value=error):
            printed = self.capture_print(get_and_display_weather, "xyz123")
            self.assertIn("Error: City not found. Please enter a valid city.", printed)


if __name__ == "__main__":
    unittest.main()
