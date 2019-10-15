from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение переменной x и считаем математическую функцию от x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # вводим ответ в текстовое поле - как тут оформляем переменную?
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    # отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    # выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    # нажать на кнопку Submit
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
