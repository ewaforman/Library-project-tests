import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', "jjj")
        self.assertEqual(formatted_name, 'Janis Jjj Joplin')


if __name__ == "__main__":
    unittest.main()