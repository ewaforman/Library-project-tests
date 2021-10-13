from selenium import webdriver
from time import sleep

# smoke test
driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe')
driver.get('https://wp.pl')

title = driver.title
print(title)

assert title == 'Wirtualna Polska - Wszystko co ważne - www.wp.pl'

sleep(2)

driver.close()


