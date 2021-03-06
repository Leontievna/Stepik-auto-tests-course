import unittest
from selenium import webdriver
import time

class TestFillRegistration(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element_by_css_selector(".first_block input.first")
        element1.send_keys("Мой ответ")
        element2 = browser.find_element_by_css_selector(".first_block input.second")
        element2.send_keys("Мой ответ")
        element3 = browser.find_element_by_css_selector(".first_block input.third")
        element3.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Should be absolute value")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element_by_css_selector(".first_block input.first")
        element1.send_keys("Мой ответ")
        element2 = browser.find_element_by_css_selector(".first_block input.second")
        element2.send_keys("Мой ответ")
        element3 = browser.find_element_by_css_selector(".first_block input.third")
        element3.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Should be absolute value")

if __name__ == "__main__":
    unittest.main()



