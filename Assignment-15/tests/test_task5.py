import io
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

from task5 import get_display_and_store_weather


class TestTask5(unittest.TestCase):
    def capture_print(self, func, *args, **kwargs):
        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            result = func(*args, **kwargs)
            return result, buf.getvalue()
        finally:
            sys.stdout = old_stdout

    def test_success_appends_and_prints(self):
        payload = {
            "name": "New York",
            "main": {"temp": 22.4, "humidity": 55},
            "weather": [{"description": "few clouds"}],
        }

        with tempfile.TemporaryDirectory() as td:
            filename = os.path.join(td, "results.json")

            with mock.patch("task5.get_weather_with_handling", return_value=payload):
                rec, printed = self.capture_print(get_display_and_store_weather, "New York", None, filename)

                # function returns the record
                self.assertIsInstance(rec, dict)
                self.assertEqual(rec.get("city"), "New York")
                self.assertEqual(rec.get("temp"), 22)
                self.assertEqual(rec.get("humidity"), 55)
                self.assertEqual(rec.get("weather"), "Few Clouds")

                # printed output contains the friendly summary
                self.assertIn("City: New York", printed)

                # file created and contains array with one record
                with open(filename, "r", encoding="utf-8") as fh:
                    arr = json.load(fh)
                self.assertIsInstance(arr, list)
                self.assertEqual(len(arr), 1)
                self.assertEqual(arr[0]["city"], "New York")

                # call again and ensure append
                rec2, _ = self.capture_print(get_display_and_store_weather, "New York", None, filename)
                with open(filename, "r", encoding="utf-8") as fh:
                    arr2 = json.load(fh)
                self.assertEqual(len(arr2), 2)

    def test_invalid_city_not_stored(self):
        error = {"error": "http_error", "status_code": 404, "body": {"message": "city not found"}}

        with tempfile.TemporaryDirectory() as td:
            filename = os.path.join(td, "results.json")

            with mock.patch("task5.get_weather_with_handling", return_value=error):
                rec, printed = self.capture_print(get_display_and_store_weather, "xyz123", None, filename)

                self.assertIsNone(rec)
                self.assertIn("Error: City not found", printed)
                # file shouldn't exist
                self.assertFalse(os.path.exists(filename))


if __name__ == "__main__":
    unittest.main()
