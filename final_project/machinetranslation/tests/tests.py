import unittest
from translator import english_to_french, french_to_english
class TestEnglishToFrench(unittest.TestCase):
    def test_english(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
    def test_not_eq(self):
        self.assertNotEqual(english_to_french("hello"), "hello")
    def test_exception_english(self):
        with self.assertRaises(TypeError):
            english_to_french()

class TestFrenchToEnglish(unittest.TestCase):
    def test_french(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
    def test_not_eq(self):
        self.assertNotEqual(french_to_english("bonjour"), "bonjour")
    def test_exception_french(self):
        with self.assertRaises(TypeError):
            french_to_english()

unittest.main()