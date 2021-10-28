import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
import random


class StudentTestCase(unittest.TestCase):
    def test_add_new_hire_success(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        self.driver.get('http://localhost:8080/books.html')

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
        sleep(5)
        id_book_hires = self.driver.find_elements_by_id("book_id")
        book_id = id_book_hires[-1].text
        self.driver.close()

        self.driver_hire = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        self.driver_hire.get('http://localhost:8080/hires.html')

        id_book = self.driver_hire.find_element_by_name("id_book")
        id_student = self.driver_hire.find_element_by_name("id_student")
        date_hire = self.driver_hire.find_element_by_name("date_hire")

        id_book.send_keys(book_id)
        id_student.send_keys(23)
        date_hire.send_keys('20/10/2021')

        sleep(2)

        add_hire_button = self.driver_hire.find_element_by_xpath("//button[@type='submit']")
        add_hire_button.click()
        sleep(1)

        message = self.driver_hire.find_element_by_id("add_hire_answer_id").text
        self.assertEqual(message, 'Wypożyczyłeś książkę.')
        self.driver_hire.close()

    def test_add_new_hire_failure(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        self.driver.get('http://localhost:8080/books.html')

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
        sleep(5)
        id_book_hires = self.driver.find_elements_by_id("book_id")
        book_id = id_book_hires[-1].text
        self.driver.close()

        self.driver_hire = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                            options=chrome_options)
        self.driver_hire.get('http://localhost:8080/hires.html')

        id_book = self.driver_hire.find_element_by_name("id_book")
        id_student = self.driver_hire.find_element_by_name("id_student")
        date_hire = self.driver_hire.find_element_by_name("date_hire")

        id_book.send_keys(book_id)
        id_student.send_keys(23)
        date_hire.send_keys('20/10/2021')

        sleep(2)

        add_hire_button = self.driver_hire.find_element_by_xpath("//button[@type='submit']")
        add_hire_button.click()
        sleep(2)

        self.driver_hire.close()

        self.driver_hire_failure = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                            options=chrome_options)
        self.driver_hire_failure.get('http://localhost:8080/hires.html')

        id_book = self.driver_hire_failure.find_element_by_name("id_book")
        id_student = self.driver_hire_failure.find_element_by_name("id_student")
        date_hire = self.driver_hire_failure.find_element_by_name("date_hire")

        id_book.send_keys(book_id)
        id_student.send_keys(23)
        date_hire.send_keys('20/10/2021')

        sleep(2)

        add_hire_button = self.driver_hire_failure.find_element_by_xpath("//button[@type='submit']")
        add_hire_button.click()
        sleep(1)

        message = self.driver_hire_failure.find_element_by_id("add_hire_answer_id").text
        self.assertEqual(message, 'Ta książka jest już wypożyczona.')

        self.driver_hire_failure.close()

    def tearDown(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        self.driver.get('http://localhost:8080/books.html')

        id_book_hires = self.driver.find_elements_by_id("book_id")
        book_id = id_book_hires[-1].text

        book_id_delete = self.driver.find_element_by_name("id")
        book_id_delete.send_keys(book_id)
        sleep(2)
        delete_book_button = self.driver.find_element_by_id("delete_book_id")
        delete_book_button.click()
        sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()