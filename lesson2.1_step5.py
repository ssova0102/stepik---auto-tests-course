from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()
	
finally:
    time.sleep(10)
    browser.quit()