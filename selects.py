from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

try:
   firstVal = int(browser.find_element_by_id("num1").text) # получаем текстовое содержимое элемента 1 по ID и преобразуем в число
   secondVal = int(browser.find_element_by_id("num2").text) # получаем текстовое содержимое элемента 2 по ID и преобразуем в число
   sum = firstVal + secondVal # получаем сумму
   select = Select(browser.find_element_by_tag_name("select")) # находим элемент select
   select.select_by_visible_text(str(sum)) # вставляем значение суммы с преобразованием в текст

   button = browser.find_element_by_class_name("btn") # находим кнопку
   button.click() # жмем!!!
   

finally:
   time.sleep(10)
   browser.quit()