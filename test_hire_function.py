import unittest
from converter_test import Conventer


class StudentTestCase(unittest.TestCase):
    def test_add_new_hire_success(self):
        converter = Conventer()
        book_id = converter.add_book()

        message = converter.add_hire(book_id)
        self.assertEqual(message, 'Wypożyczyłeś książkę.')

    def test_add_new_hire_failure(self):
        converter = Conventer()
        book_id = converter.add_book()

        converter.add_hire(book_id)
        message = converter.add_hire(book_id)

        self.assertEqual(message, 'Ta książka jest już wypożyczona.')

    def test_return_hire_success(self):
        converter = Conventer()
        book_id = converter.add_book()

        converter.add_hire(book_id)

        message = converter.return_book(book_id)

        self.assertEqual(message, 'Ksiazka zostala oddana.')

    def tearDown(self):
        converter = Conventer()
        converter.delete_book()


if __name__ == "__main__":
    unittest.main()