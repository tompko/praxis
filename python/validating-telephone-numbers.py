import re
import unittest

patterns = [ "^\d{3}[ -.]?\d{4}$",
             "^\d{3}(?P<sep>[ -.])?\d{3}(?P=sep)?\d{4}$",
             "^\(\d{3}\) ?\d{3}[ -.]?\d{4}$"]

def validate_telephone_number(number):
    for pattern in patterns:
        if re.match(pattern, number):
            return number
    return None

class TestPhoneNumbers(unittest.TestCase):

    def test_valid(self):
        numbers = ["1234567890",
                   "123-456-7890",
                   "123.456.7890",
                   "(123)456-7890",
                   "(123) 456-7890",
                   "456-7890"]
        for num in numbers:
            self.assertEqual(validate_telephone_number(num), num)

    def test_invalid(self):
        numbers = ["12-345-6789",
                   "123-45-6789",
                   "123-456-789",
                   "123-45-67890",
                   "123:4567890",
                   "123/456-7890",
                   "123456",
                   "12345678",
                   "123456789",
                   "12345678901",
                   "123-456-7890 x123"]
        
        for num in numbers:
            self.assertEqual(validate_telephone_number(num), None)

if __name__ == "__main__":
    unittest.main()
