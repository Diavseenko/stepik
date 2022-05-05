from selenium import webdriver
import time
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
   browser=webdriver.Chrome()
   browser.get(link)

   button = browser.find_element_by_class_name("btn")
   button.click()

   modal = browser.switch_to.alert
   modal.accept()

   elemX = browser.find_element_by_id("input_value").text
   

   key = calc(int(elemX))

   inputField = browser.find_element_by_id("answer")
   inputField.send_keys(key)

   sendButt = browser.find_element_by_class_name("btn")

   
   sendButt.click()


finally:
   time.sleep(5)
   browser.quit()   


