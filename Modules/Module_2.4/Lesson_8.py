from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # level 1
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    button.click()

    # level 2
    text = browser.find_element_by_id("input_value").text
    input_el = browser.find_element_by_id("answer")
    input_el.send_keys(calc(text))
    
    button_answer = browser.find_element_by_id("solve")
    button_answer.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
