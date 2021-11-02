import unittest
from selenium import webdriver
from time import sleep
from converter_test import Conventer


class BookTestCase(unittest.TestCase):
    def setUp(self):
        converter = Conventer()
        chrome_options = converter.add_chrome_options()

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                  options=chrome_options)
        self.driver.get('http://localhost:8080/books.html')

    def test_add_new_book_success(self):
        author_name = self.driver.find_element_by_name("name")
        author_surname = self.driver.find_element_by_name("surname")
        title_book = self.driver.find_element_by_name("title")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_name.send_keys(name)
        author_surname.send_keys(surname)
        title_book.send_keys(title)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Dodano nową książkę.')

    def test_add_new_book_failure_empty_fields(self):
        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_name(self):
        author_name = self.driver.find_element_by_name("name")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_name.send_keys(name)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_surname(self):
        author_surname = self.driver.find_element_by_name("surname")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_surname.send_keys(surname)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_title(self):
        title_book = self.driver.find_element_by_name("title")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        title_book.send_keys(title)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_name_and_surname(self):
        author_name = self.driver.find_element_by_name("name")
        author_surname = self.driver.find_element_by_name("surname")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_name.send_keys(name)
        author_surname.send_keys(surname)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_name_and_title(self):
        author_name = self.driver.find_element_by_name("name")
        title_book = self.driver.find_element_by_name("title")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_name.send_keys(name)
        title_book.send_keys(title)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_add_new_book_failure_only_surname_and_title(self):
        author_surname = self.driver.find_element_by_name("surname")
        title_book = self.driver.find_element_by_name("title")

        converter = Conventer()
        name, surname, title = converter.get_random_name_surname_title()

        author_surname.send_keys(surname)
        title_book.send_keys(title)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Wypełnij wszystkie pola.')

    def test_delete_book_not_in_database(self):
        book_id = self.driver.find_element_by_name("id")
        book_id.send_keys("0")
        delete_student_button = self.driver.find_element_by_id("delete_book_id")
        delete_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("delete_book_answer_id").text
        self.assertEqual(message, 'Nie ma takiej książki w bazie.')

    def test_delete_book_in_database(self):
        book_id = self.driver.find_element_by_name("id")
        number = self.driver.find_element_by_tag_name("td").text
        number_int = int(number)
        book_id.send_keys(number_int)
        delete_book_button = self.driver.find_element_by_id("delete_book_id")
        delete_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("delete_book_answer_id").text
        self.assertEqual(message, 'Usunięto książkę.')

    def test_select_book_by_id_in_data_base(self):
        book_id = self.driver.find_element_by_id("book_id").text
        id_input = self.driver.find_element_by_id("input_book_id")
        id_input.send_keys(book_id)
        select_book_button = self.driver.find_element_by_id("find_book_id")
        select_book_button.click()
        sleep(1)
        number_of_elements = len(self.driver.find_elements_by_id("book_id"))
        self.assertEqual(number_of_elements, 1)

    def test_select_book_by_id_not_in_data_base(self):
        id_input = self.driver.find_element_by_id("input_book_id")
        id_input.send_keys(0)
        select_book_button = self.driver.find_element_by_id("find_book_id")
        select_book_button.click()
        sleep(1)
        number_of_elements = len(self.driver.find_elements_by_id("book_id"))
        self.assertEqual(number_of_elements, 0)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()