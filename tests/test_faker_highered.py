import unittest
from faker.generator import Generator
from config import Provider


class HigheredProviderTestCase(unittest.TestCase):
    """Provider test case."""

    def setUp(self):
        self.provider = Provider(Generator())

    def test_lists_in_order(self):
        """Test interal values are in order."""
        for attr_name, attr in self.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assert_list_in_order(attr)

    def assert_list_in_order(self, the_list):
        """Assert a list is in order."""
        prev_value = ""
        for this_value in the_list:
            self.assertGreaterEqual(this_value, prev_value)
            prev_value = this_value

    def test_no_duplicates(self):
        """Test value lists don't contain duplicates."""
        for attr_name, attr in self.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assertEqual(len(attr), len(set(attr)))

    def test_words(self):
        """Test that generated string is at least two words long."""
        name = self.provider.institution_name()
        word_count = len(name.split())
        self.assertGreaterEqual(word_count, 2)


if __name__ == "__main__":
    unittest.main()