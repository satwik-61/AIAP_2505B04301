import unittest
from datetime import datetime

def convert_date_format(date_str: str) -> str:
    """
    Convert a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY'.
    Raises:
        TypeError: If date_str is not a string.
        ValueError: If date_str is not in the expected format or invalid date.
    """
    if not isinstance(date_str, str):
        raise TypeError("Date must be provided as a string.")
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Date must be in 'YYYY-MM-DD' format and valid.") from exc
    return parsed_date.strftime("%d-%m-%Y")

class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2025-11-13"), "13-11-2025")

    def test_single_digit_month_and_day(self):
        self.assertEqual(convert_date_format("2023-01-05"), "05-01-2023")

    def test_leap_year(self):
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("13-11-2025")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            convert_date_format(20231113)

if __name__ == "__main__":
    unittest.main(exit=False)
    try:
        user_input = input("Enter a date in YYYY-MM-DD format (press Enter to skip): ").strip()
        if user_input:
            try:
                converted = convert_date_format(user_input)
                print(f"Converted date: {converted}")
            except (TypeError, ValueError) as exc:
                print(f"Invalid input: {exc}")
    except EOFError:
        pass

