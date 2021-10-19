import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
import random


class BookTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                  options=chrome_options)
        self.driver.get('http://localhost:8080/books.html')

    def test_add_new_book(self):
        author_name = self.driver.find_element_by_name("name")
        author_surname = self.driver.find_element_by_name("surname")
        title_book = self.driver.find_element_by_name("title")

        letters = list(string.ascii_lowercase)
        surname = (''.join(random.choice(letters) for i in range(10)).title())
        name = (''.join(random.choice(letters) for i in range(6)).title())
        title = (''.join(random.choice(letters) for i in range(10)).title())

        author_name.send_keys(name)
        author_surname.send_keys(surname)
        title_book.send_keys(title)

        add_book_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_book_answer_id").text
        self.assertEqual(message, 'Dodano nową książkę.')

    # def test_add_new_student_already_in_database(self):
    #     student_name = self.driver.find_element_by_name("name")
    #     student_surname = self.driver.find_element_by_name("surname")
    #     student_username = self.driver.find_element_by_name("username")
    #
    #     student_name.send_keys("Emila")
    #     student_surname.send_keys("Witkowska")
    #     student_username.send_keys("EmWit")
    #
    #     add_student_button = self.driver.find_element_by_xpath("//button[@type='submit']")
    #     add_student_button.click()
    #     sleep(1)
    #
    #     message = self.driver.find_element_by_id("add_student_answer_id").text
    #     self.assertEqual(message, 'Taki student jest juz w bazie.')
    #
    # def test_delete_student_not_in_database(self):
    #     student_name = self.driver.find_element_by_name("id")
    #     student_name.send_keys("1")
    #     delete_student_button = self.driver.find_element_by_id("delete_student_id")
    #     delete_student_button.click()
    #     sleep(1)
    #
    #     message = self.driver.find_element_by_id("delete_student_answer_id").text
    #     self.assertEqual(message, 'Nie ma takiego studenta w bazie.')
    #
    # def test_delete_student_in_database(self):
    #     student_name = self.driver.find_element_by_name("id")
    #     number = self.driver.find_element_by_tag_name("td").text
    #     number_int = int(number)
    #     student_name.send_keys(number_int)
    #     delete_student_button = self.driver.find_element_by_id("delete_student_id")
    #     delete_student_button.click()
    #     sleep(1)
    #
    #     message = self.driver.find_element_by_id("delete_student_answer_id").text
    #     self.assertEqual(message, 'Usunięto studenta.')
    #
    # def test_select_student_by_username_in_data_base(self):
    #     student_username = self.driver.find_element_by_id("username_id").text
    #     username_input = self.driver.find_element_by_id("input_username_id")
    #     username_input.send_keys(student_username)
    #     find_student_button = self.driver.find_element_by_id("find_student_id")
    #     find_student_button.click()
    #     sleep(1)
    #     number_of_elements = len(self.driver.find_elements_by_id("username_id"))
    #     self.assertEqual(number_of_elements, 1)
    #
    # def test_select_student_by_username_not_in_data_base(self):
    #     username_input = self.driver.find_element_by_id("input_username_id")
    #     username_input.send_keys("student_username")
    #     find_student_button = self.driver.find_element_by_id("find_student_id")
    #     find_student_button.click()
    #     sleep(1)
    #     number_of_elements = len(self.driver.find_elements_by_id("username_id"))
    #     self.assertEqual(number_of_elements, 0)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()