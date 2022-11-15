import unittest
from translator import englishtofrench, frenchtoenglish


class TestTranslation(unittest.TestCase):
    def test_en_fr(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("How"), "Comment")

    def test_fr_en(self):
        self.assertEqual(frenchtoenglish("Aujourd'hui"), "Today")
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")


class TestNoAttribute(unittest.TestCase):
    def test_en_fr(self):
        self.assertEqual(englishtofrench(), "an english text is needed as input.")

    def test_fr_en(self):
        self.assertEqual(frenchtoenglish(), "an french text is needed as input.")


if __name__ == '__main__':
    unittest.main()
