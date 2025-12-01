import io
import json
import sys
import unittest
from unittest import mock

import requests

from task2 import get_weather_with_handling


class TestGetWeatherWithHandling(unittest.TestCase):
    def capture_print(self, func, *args, **kwargs):
        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            result = func(*args, **kwargs)
            output = buf.getvalue()
        finally:
            sys.stdout = old_stdout
        return result, output

    def test_missing_api_key(self):
        result, output = self.capture_print(get_weather_with_handling, "London", api_key=None)
        self.assertIn("missing_api_key", json.dumps(result))
        self.assertIn("missing_api_key", output)

    def test_request_exception(self):
        with mock.patch("requests.get", side_effect=requests.exceptions.RequestException("conn fail")):
            result, output = self.capture_print(get_weather_with_handling, "Paris", api_key="DUMMY")
            self.assertEqual(result.get("error"), "request_exception")
            self.assertIn("conn fail", json.dumps(result))

    def test_http_error_with_json_body(self):
        mock_resp = mock.Mock()
        mock_resp.status_code = 401
        mock_resp.json.return_value = {"cod": 401, "message": "Invalid API key"}

        with mock.patch("requests.get", return_value=mock_resp):
            result, output = self.capture_print(get_weather_with_handling, "Berlin", api_key="BADKEY")
            self.assertEqual(result.get("error"), "http_error")
            self.assertEqual(result.get("status_code"), 401)

    def test_http_error_with_non_json_body(self):
        mock_resp = mock.Mock()
        mock_resp.status_code = 404
        mock_resp.json.side_effect = ValueError("No JSON")
        mock_resp.text = "Not found"

        with mock.patch("requests.get", return_value=mock_resp):
            result, output = self.capture_print(get_weather_with_handling, "QWERTY", api_key="DUMMY")
            self.assertEqual(result.get("error"), "http_error")
            self.assertEqual(result.get("body", {}).get("raw_text"), "Not found")

    def test_success(self):
        expected = {"weather": [{"main": "Clear"}], "main": {"temp": 20}}
        mock_resp = mock.Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = expected

        with mock.patch("requests.get", return_value=mock_resp):
            result, output = self.capture_print(get_weather_with_handling, "Sydney", api_key="OK")
            self.assertEqual(result, expected)
            # printed JSON should contain the weather key
            self.assertIn("weather", output)

    def test_invalid_json_on_ok_status(self):
        mock_resp = mock.Mock()
        mock_resp.status_code = 200
        mock_resp.json.side_effect = ValueError("bad json")
        mock_resp.text = "<html>bad</html>"

        with mock.patch("requests.get", return_value=mock_resp):
            result, output = self.capture_print(get_weather_with_handling, "Tokyo", api_key="OK")
            self.assertEqual(result.get("error"), "invalid_json")


if __name__ == "__main__":
    unittest.main()
