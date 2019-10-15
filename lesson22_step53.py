from selenium import webdriver
import time
import math

try:
    # открыть страницу
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # считать значение для переменной x
    x_value = browser.find_element_by_css_selector("#input_value")
    x = x_value.text
    # посчитать математическую функцию от x
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    # ввести ответ в текстовое поле
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    # выбрать чекбокс "I'm the robot"
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    # проскорллить страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # переключить radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    # нажать на кнопку "Submit"
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
