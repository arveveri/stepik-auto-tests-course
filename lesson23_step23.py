from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("prompt('Are you a teapot?', 'No');")
    time.sleep(2)
    # переключиться на промпт
    prompt = browser.switch_to.alert
    # ввести текст в промпт
    prompt.send_keys("Yes")
    prompt.accept()
    #prompt.dismiss()

finally:
    time.sleep(3)
    browser.quit()
