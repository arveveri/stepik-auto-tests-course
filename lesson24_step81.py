from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    button_book = browser.find_element_by_id("book")
    button_book.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x_value = browser.find_element_by_css_selector("#input_value")
    x = x_value.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
