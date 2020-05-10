import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_open_link(browser, link):
    link = f"{link}/"
    browser.get(link)

    answer = str(math.log(int(time.time())))

    element1 = browser.find_element(By.CLASS_NAME, "textarea")
    element1.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert "Correct!" in message.text