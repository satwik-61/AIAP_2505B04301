import io
import sys
import unittest

from task3 import extract_weather_fields, display_weather_summary


class TestTask3(unittest.TestCase):
    def capture_print(self, func, *args, **kwargs):
        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            func(*args, **kwargs)
            return buf.getvalue()
        finally:
            sys.stdout = old_stdout

    def test_extract_full(self):
        payload = {
            "name": "London",
            "main": {"temp": 18.3, "humidity": 60},
            "weather": [{"description": "clear sky"}],
        }
        out = extract_weather_fields(payload)
        self.assertEqual(out["city"], "London")
        self.assertEqual(out["temperature"], "18°C")
        self.assertEqual(out["humidity"], "60%")
        self.assertEqual(out["description"], "Clear Sky")

    def test_extract_missing_fields(self):
        payload = {"main": {}}
        out = extract_weather_fields(payload)
        self.assertIsNone(out["city"])
        self.assertIsNone(out["temperature"])
        self.assertIsNone(out["humidity"])
        self.assertIsNone(out["description"])

    def test_display_prints_nice_text(self):
        payload = {
            "name": "London",
            "main": {"temp": 18.3, "humidity": 60},
            "weather": [{"description": "clear sky"}],
        }
        printed = self.capture_print(display_weather_summary, payload)
        self.assertIn("City: London", printed)
        self.assertIn("Temperature: 18°C", printed)
        self.assertIn("Humidity: 60%", printed)
        self.assertIn("Weather: Clear Sky", printed)


if __name__ == "__main__":
    unittest.main()
