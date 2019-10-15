from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Hello!');")
    # переключиться на алерт
    alert = browser.switch_to.alert
    # получить текст алерта
    alert_text = alert.text
    time.sleep(2)
    # принять алерт
    alert.accept()
    print (alert_text)

finally:
    time.sleep(2)
    browser.quit()
