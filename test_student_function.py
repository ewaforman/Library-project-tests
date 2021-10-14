import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import string
import random


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-site-isolation-trials")

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe',
                                  options=chrome_options)
        self.driver.get('http://localhost:8080')

    def test_add_new_student(self):
        student_name = self.driver.find_element_by_name("name")
        student_surname = self.driver.find_element_by_name("surname")
        student_username = self.driver.find_element_by_name("username")

        letters = list(string.ascii_lowercase)
        surname = (''.join(random.choice(letters) for i in range(10)).title())
        username = (''.join(random.choice(letters) for i in range(6)).title())

        student_name.send_keys("Emilia")
        student_surname.send_keys(surname)
        student_username.send_keys(username)

        add_student_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_student_answer_id").text
        self.assertEqual(message, 'Dodałeś nowego studenta.')

    def test_add_new_student_already_in_database(self):
        student_name = self.driver.find_element_by_name("name")
        student_surname = self.driver.find_element_by_name("surname")
        student_username = self.driver.find_element_by_name("username")

        student_name.send_keys("Emila")
        student_surname.send_keys("Witkowska")
        student_username.send_keys("EmWit")

        add_student_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_student_answer_id").text
        self.assertEqual(message, 'Taki student jest juz w bazie.')

    def test_delete_student_not_in_database(self):
        student_name = self.driver.find_element_by_name("id")
        student_name.send_keys("1")
        delete_student_button = self.driver.find_element_by_id("delete_student_id")
        delete_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("delete_student_answer_id").text
        self.assertEqual(message, 'Nie ma takiego studenta w bazie.')

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()