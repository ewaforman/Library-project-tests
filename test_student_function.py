import unittest
from selenium import webdriver
from time import sleep
from converter_test import Conventer


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        converter = Conventer()
        chrome_options = converter.add_chrome_options()

        self.driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32_5/chromedriver.exe',
                                  options=chrome_options)
        self.driver.get('http://localhost:8080')

    def test_add_new_student(self):
        student_name = self.driver.find_element_by_name("name")
        student_surname = self.driver.find_element_by_name("surname")
        student_username = self.driver.find_element_by_name("username")

        converter = Conventer()
        name, surname, username = converter.get_random_name_surname_username()

        student_name.send_keys(name)
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

        name = self.driver.find_element_by_id("name_id").text
        surname = self.driver.find_element_by_id("surname_id").text
        username = self.driver.find_element_by_id("username_id").text

        student_name.send_keys(name)
        student_surname.send_keys(surname)
        student_username.send_keys(username)

        add_student_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        add_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("add_student_answer_id").text
        self.assertEqual(message, 'Taki student jest juz w bazie.')

    def test_delete_student_not_in_database(self):
        student_id = self.driver.find_element_by_name("id")
        student_id.send_keys("0")
        delete_student_button = self.driver.find_element_by_id("delete_student_id")
        delete_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("delete_student_answer_id").text
        self.assertEqual(message, 'Nie ma takiego studenta w bazie.')

    def test_delete_student_in_database(self):
        student_id = self.driver.find_element_by_name("id")
        number = self.driver.find_element_by_tag_name("td").text
        number_int = int(number)
        student_id.send_keys(number_int)
        delete_student_button = self.driver.find_element_by_id("delete_student_id")
        delete_student_button.click()
        sleep(1)

        message = self.driver.find_element_by_id("delete_student_answer_id").text
        self.assertEqual(message, 'Usunięto studenta.')

    def test_select_student_by_username_in_data_base(self):
        student_username = self.driver.find_element_by_id("username_id").text
        username_input = self.driver.find_element_by_id("input_username_id")
        username_input.send_keys(student_username)
        find_student_button = self.driver.find_element_by_id("find_student_id")
        find_student_button.click()
        sleep(1)
        number_of_elements = len(self.driver.find_elements_by_id("username_id"))
        self.assertEqual(number_of_elements, 1)

    def test_select_student_by_username_not_in_data_base(self):
        username_input = self.driver.find_element_by_id("input_username_id")
        username_input.send_keys("&&&")
        find_student_button = self.driver.find_element_by_id("find_student_id")
        find_student_button.click()
        sleep(1)
        number_of_elements = len(self.driver.find_elements_by_id("username_id"))
        self.assertEqual(number_of_elements, 0)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()