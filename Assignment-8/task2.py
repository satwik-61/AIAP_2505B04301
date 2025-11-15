import unittest

def assign_grade(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive.")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

class TestAssignGrade(unittest.TestCase):
    def test_grade_a_boundaries(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(100), "A")

    def test_grade_b_boundaries(self):
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(89), "B")

    def test_grade_c_boundaries(self):
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(79), "C")

    def test_grade_d_boundaries(self):
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(69), "D")

    def test_grade_f_boundaries(self):
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(50), "F")
        self.assertEqual(assign_grade(59.9), "F")

    def test_invalid_below_zero(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)

    def test_invalid_above_hundred(self):
        with self.assertRaises(ValueError):
            assign_grade(105)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            assign_grade("eighty")

if __name__ == "__main__":
    unittest.main(exit=False)
    try:
        user_input = input("Enter a score between 0 and 100 (press Enter to skip): ").strip()
        if user_input:
            try:
                numeric_score = float(user_input)
                grade = assign_grade(numeric_score)
                print(f"Grade: {grade}")
            except (TypeError, ValueError) as exc:
                print(f"Invalid input: {exc}")
    except EOFError:
        pass

