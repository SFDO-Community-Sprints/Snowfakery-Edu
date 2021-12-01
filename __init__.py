
from faker import Faker
from faker.generator import Generator
import faker.providers.address.en_US
import faker.providers.lorem.en_US
import faker.providers.company
import json
import unittest

fake = Faker()
fakeAddress = faker.providers.address.en_US.Provider(Generator())
fakeLorem = faker.providers.lorem.en_US.Provider(Generator())
fakeCompany = faker.providers.company.Provider(Generator())

INSTITUTIONTYPES = {
    'University',
    'College',
    'Junior College',
    'State College'
}

TOPICS = {
    'Cloud',
    'ABC',
    'Computing',
    'Friendly',
    'Sunshine',
    'XYZ',
    'Rainbow',
    'Synergy',
    'Supernova'
}


class Provider(faker.providers.BaseProvider):
    def institution_name(self):
        """Fake higher ed names."""
        suffix = self.random_element(INSTITUTIONTYPES)
        topic = self.random_element(TOPICS)
        return " ".join([topic, suffix]).strip()

    def department_name(self):
        f = open('recipes/plugins/faker_highered/HigherEdDepartments.json')
        depts = json.load(f)
        deptnames = set()
        for item in depts:
            printme = item["title"]
            deptnames.add(printme)
        return self.random_element(deptnames)


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
