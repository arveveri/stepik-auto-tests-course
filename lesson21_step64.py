from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # атрибут "disabled" с помощью встроенного метода get_attribute и проверим его значение
    button = browser.find_element_by_css_selector(".btn")
    button_disabled = button.get_attribute("disabled")
    print("value of button: ", button_disabled)
    assert button_disabled is None, "Button is not disabled by default"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
