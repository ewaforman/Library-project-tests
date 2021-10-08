from selenium import webdriver
from time import sleep
import login

driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://profil.wp.pl/login/login.html')

wp_login = login.wp_login
wp_password = login.wp_password

username_input = driver.find_element_by_id("login")
password_input = driver.find_element_by_id("password")

username_input.send_keys(wp_login)
password_input.send_keys(wp_password)

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
driver.implicitly_wait(20)

newMessage_button = driver.find_element_by_xpath("//button[@href='#/draft?type=new']")
newMessage_button.click()

send_to = driver.find_element_by_xpath("//div[@class='flex-max sc-lcpuFF bXaSDj']//input")
send_to.click()
send_to.send_keys('ewaforman@gmail.com')

subject = driver.find_element_by_xpath("//input[@name='subject']")
subject.click()
subject.send_keys('pogoda')

sleep(5)

driver.close()