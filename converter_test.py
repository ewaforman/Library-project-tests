from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
import random
from datetime import datetime


class Conventer:
    def add_chrome_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")
        return chrome_options

    def add_book(self):
        chrome_options = self.add_chrome_options()

        driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        driver.get('http://localhost:8080/books.html')

        author_name = driver.find_element_by_name("name")
        author_surname = driver.find_element_by_name("surname")
        title_book = driver.find_element_by_name("title")

        name, surname, title = self.get_random_name_surname_title()

        author_name.send_keys(name)
        author_surname.send_keys(surname)
        title_book.send_keys(title)

        add_book_button = driver.find_element_by_xpath("//button[@type='submit']")
        add_book_button.click()
        sleep(5)
        id_book_hires = driver.find_elements_by_id("book_id")
        book_id = id_book_hires[-1].text
        driver.close()
        return book_id

    def add_hire(self, book_id):
        chrome_options = self.add_chrome_options()
        self.driver_hire = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                            options=chrome_options)
        self.driver_hire.get('http://localhost:8080/hires.html')

        today_date = self.get_date()

        id_book = self.driver_hire.find_element_by_name("id_book")
        id_student = self.driver_hire.find_element_by_name("id_student")
        date_hire = self.driver_hire.find_element_by_name("date_hire")

        id_book.send_keys(book_id)
        id_student.send_keys(23)
        date_hire.send_keys(today_date)

        sleep(2)

        add_hire_button = self.driver_hire.find_element_by_xpath("//button[@type='submit']")
        add_hire_button.click()
        sleep(1)

        message = self.driver_hire.find_element_by_id("add_hire_answer_id").text
        self.driver_hire.close()
        return message

    def delete_book(self):
        chrome_options = self.add_chrome_options()

        driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                       options=chrome_options)
        driver.get('http://localhost:8080/books.html')

        id_book_hires = driver.find_elements_by_id("book_id")
        book_id = id_book_hires[-1].text

        book_id_delete = driver.find_element_by_name("id")
        book_id_delete.send_keys(book_id)
        sleep(2)
        delete_book_button = driver.find_element_by_id("delete_book_id")
        delete_book_button.click()
        sleep(5)
        driver.close()

    def return_book(self, book_id):
        chrome_options = self.add_chrome_options()
        self.driver_hire = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                            options=chrome_options)
        self.driver_hire.get('http://localhost:8080/hires.html')

        today_date = self.get_date()

        id_book = self.driver_hire.find_element_by_name("id_book_return")
        date_return = self.driver_hire.find_element_by_name("date_return")

        id_book.send_keys(book_id)
        date_return.send_keys(today_date)

        sleep(2)

        return_button = self.driver_hire.find_element_by_id("button_return_id")
        return_button.click()
        sleep(1)

        message = self.driver_hire.find_element_by_id("answer_return_id").text
        self.driver_hire.close()
        return message

    def get_random_name_surname_title(self):
        letters = list(string.ascii_lowercase)
        surname = (''.join(random.choice(letters) for i in range(10)).title())
        name = (''.join(random.choice(letters) for i in range(6)).title())
        title = (''.join(random.choice(letters) for i in range(10)).title())
        return name, surname, title

    def get_random_name_surname_username(self):
        letters = list(string.ascii_lowercase)
        surname = (''.join(random.choice(letters) for i in range(10)).title())
        name = (''.join(random.choice(letters) for i in range(6)).title())
        username = (''.join(random.choice(letters) for i in range(7)).title())
        return name, surname, username

    def get_date(self):
        today = datetime.now()
        string_today = today.strftime('%d/%m/%Y')
        return string_today
