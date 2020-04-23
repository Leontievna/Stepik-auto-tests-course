
from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    element1 = browser.find_element_by_id("answer")
    element1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

#    people_radio = browser.find_element_by_id("peopleRule")
#    people_checked = people_radio.get_attribute("checked")
#    assert people_checked == "true", "People radio is selected by default"

#    robots_radio = browser.find_element_by_id("robotsRule")
#    robots_checked = robots_radio.get_attribute("checked")
#    assert robots_checked is None

#    button = browser.find_element_by_css_selector("button.btn")
#    button_checked = button.get_attribute("disabled")
#    print("value of robots radio: ", button_checked)
#    assert button_checked == "disabled", "Button is disabled by default"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()