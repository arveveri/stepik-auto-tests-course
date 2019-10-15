from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    #link="http://suninjuly.github.io/selects1.html"
    link="http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим и забираем слагаемые через browser.get_attribute
    num1 = browser.find_element_by_css_selector("#num1")
    n1 = num1.text
    num2 = browser.find_element_by_css_selector("#num2")
    n2 = num2.text

    # считаем сумму двух чисел
    n1n2 = str(int(n1)+int(n2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(n1n2) # ищем элемент с текстом идентичным тому, что в переменной n1n2
    #select.select_by_visible_text("text") # ищем элемент по видимому тексту
    #select.select_by_index(index) # ищем элемент по его индексу или порядковому номеру

    # нажать на кнопку Submit
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
