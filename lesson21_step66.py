from selenium import webdriver
import time
import math

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    treasure = browser.find_element_by_css_selector("#treasure")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    # считаем математическую функцию от x
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # вводим ответ в текстовое поле - как тут оформляем переменную?
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    # отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    # выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()

    # нажать на кнопку Submit
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
