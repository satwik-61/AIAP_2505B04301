import re
import unittest

def is_sentence_palindrome(sentence: str) -> bool:
    if not isinstance(sentence, str):
        raise TypeError("Sentence must be a string.")

    cleaned = re.sub(r"[^\w]", "", sentence).lower()
    return cleaned == cleaned[::-1]


class TestIsSentencePalindrome(unittest.TestCase):
    def test_classic_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))

    def test_palindrome_with_mixed_case_and_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Never odd, never even!"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_non_palindrome_sentence(self):
        self.assertFalse(is_sentence_palindrome("This definitely is not one."))

    def test_sentence_with_extra_spaces(self):
        self.assertTrue(is_sentence_palindrome("  Was it a rat I saw   "))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_sentence_palindrome(12345)

if __name__ == "__main__":
    unittest.main(exit=False)
    try:
        user_input = input("Enter a sentence to check palindrome (press Enter to skip): ")
        if user_input:
            result = is_sentence_palindrome(user_input)
            print(f"Palindrome: {result}")
    except EOFError:
        pass

