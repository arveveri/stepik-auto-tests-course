from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("confirm('Are you a teapot?');")
    time.sleep(2)
    # переключиться на конфёрм
    confirm = browser.switch_to.alert
    # принять конфёрм
    # confirm.accept()
    # отказаться от конфёрма
    confirm.dismiss()

finally:
    time.sleep(3)
    browser.quit()
