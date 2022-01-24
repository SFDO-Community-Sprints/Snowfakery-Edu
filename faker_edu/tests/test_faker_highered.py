import unittest
from faker import Faker, Generator
import faker_edu


class HigheredProviderTestCase(unittest.TestCase):
    """Provider test case."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_edu.Provider)

    def test_lists_in_order(self):
        """Test interal values are in order."""
        for attr_name, attr in faker_edu.__dict__.items():
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
        for attr_name, attr in faker_edu.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assertEqual(len(attr), len(set(attr)))

    def test_institution_name(self):
        """Test that generated institution name is at least two words long."""
        result = self.fake.institution_name()
        word_count = len(result.split())
        self.assertGreaterEqual(word_count, 2)

    def test_high_school_name(self):
        """Test that generated high school name is at least two words long."""
        result = self.fake.highschool_name()
        word_count = len(result.split())
        self.assertGreaterEqual(word_count, 2)

    def test_department_name(self):
        """Test that generated department name is from the list."""
        dept = self.fake.department_name()
        self.assertIn(dept, faker_edu.DEPARTMENTS,
                      'Generated department not from list')

    def test_position_name(self):
        """Test that generated position name is from the list."""
        pos = self.fake.faculty_position()
        self.assertIn(pos, faker_edu.FACULTYPOSITIONS,
                      'Generated faculty position not from list')

    def test_faculty_title(self):
        """Test that generated position name is from the list."""
        title = self.fake.faculty_title()
        self.assertTrue(' of ' in title, 'Missing "of" in title')
        parts = title.split(' of ')
        self.assertIn(parts[0], faker_edu.FACULTYPOSITIONS,
                      'Position segment not from position list.')
        self.assertIn(parts[1], faker_edu.DEPARTMENTS,
                      'Position segment not from department list.')


if __name__ == "__main__":
    unittest.main()
