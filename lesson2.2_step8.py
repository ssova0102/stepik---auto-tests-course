from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '123.txt')
 
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2=browser.find_element_by_name("lastname")
    input2.send_keys("Ivan")
    input3=browser.find_element_by_name("email")
    input3.send_keys("Ivan")
    txt=browser.find_element_by_name("file")
    txt.send_keys(file_path)
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
	
finally:
    time.sleep(10)
    browser.quit()