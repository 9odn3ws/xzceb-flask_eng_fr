import unittest
from translator import englishtofrench, frenchtoenglish


class TestTranslation(unittest.TestCase):
    # Unittest assertEqual english to french, last test null input.
    def test_en_fr(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("How"), "Comment")
        self.assertEqual(englishtofrench(""), "Please enter a text.")
        self.assertEqual(englishtofrench(), "a string is needed as input.")

    # Unittest assertEqual french to english, last test null input.
    def test_fr_en(self):
        self.assertEqual(frenchtoenglish("Aujourd'hui"), "Today")
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertEqual(frenchtoenglish(""), "Please enter a text.")
        self.assertEqual(frenchtoenglish(), "a string is needed as input.")


class TestNoString(unittest.TestCase):
    # Unittest assertNotEqual english to french.
    def test_en_fr(self):
        self.assertNotEqual(englishtofrench(["Hello World"]), "Hello World")
        self.assertNotEqual(englishtofrench(123), "123")

    # Unittest assertNotEqual french to english.
    def test_fr_en(self):
        self.assertNotEqual(frenchtoenglish(["Hello World"]), "Hello World")
        self.assertNotEqual(frenchtoenglish(123), "123")


if __name__ == '__main__':
    unittest.main()
