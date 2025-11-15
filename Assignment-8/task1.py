import unittest
def is_valid_email(email: str) -> bool:
    """
    Validate an email address based on the specified rules:
    - Must contain exactly one '@' symbol.
    - Must contain at least one '.' character after the '@'.
    - Must not start or end with a special character (non-alphanumeric).
    """
    if not isinstance(email, str) or not email:
        return False

    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")

    if not local_part or not domain_part:
        return False

    if "." not in domain_part:
        return False

    if not email[0].isalnum() or not email[-1].isalnum():
        return False

    if not local_part[0].isalnum() or not local_part[-1].isalnum():
        return False

    if not domain_part[0].isalnum() or not domain_part[-1].isalnum():
        return False

    return True


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "john.doe@example.com",
            "user123@sub.domain.com",
            "alice.bob@company.co.uk",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("johndoe.example.com"))

    def test_missing_dot(self):
        self.assertFalse(is_valid_email("johndoe@examplecom"))

    def test_starts_with_special_character(self):
        self.assertFalse(is_valid_email(".john@example.com"))

    def test_ends_with_special_character(self):
        self.assertFalse(is_valid_email("john@example.com."))

    def test_local_part_ends_with_special_character(self):
        self.assertFalse(is_valid_email("john.@example.com"))

    def test_domain_part_starts_with_special_character(self):
        self.assertFalse(is_valid_email("john@.example.com"))

    def test_multiple_at_symbols(self):
        self.assertFalse(is_valid_email("john@@example.com"))


if __name__ == "__main__":
    unittest.main()

