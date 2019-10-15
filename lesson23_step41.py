from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    # открыть страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # нажать на кнопку
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # принять конфёрм
    confirm = browser.switch_to.alert
    confirm.accept()

    # на новой странице решить капчу для роботов, чтобы получить число с ответом
    x_value = browser.find_element_by_css_selector("#input_value")
    x = x_value.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
