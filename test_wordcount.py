import unittest
from wordcount import count_words, count_chars, top_words


class TestCountWords(unittest.TestCase):
    def test_count_words_basic(self):
        self.assertEqual(count_words("hello world foo"), 3)

    def test_count_words_empty(self):
        self.assertEqual(count_words(""), 0)


class TestCountChars(unittest.TestCase):
    def test_count_chars_basic(self):
        self.assertEqual(count_chars("hello world"), 11)

    def test_count_chars_empty(self):
        self.assertEqual(count_chars(""), 0)


class TestTopWords(unittest.TestCase):
    def test_top_words_basic(self):
        text = "a a a b b c"
        result = top_words(text, n=2)
        self.assertEqual(result, [("a", 3), ("b", 2)])

    def test_top_words_case_insensitive(self):
        text = "The the THE dog"
        result = top_words(text, n=1)
        self.assertEqual(result, [("the", 3)])

    def test_top_words_fewer_than_n(self):
        text = "alpha beta"
        result = top_words(text, n=5)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
