import unittest

class test_1(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
    # В тексте страницы, есть два поля, содержащих class="form-control second", но только у поля с фамилией так же имеется атрибут required, соответственно, сделав составной CSS селектор, учитываюший наличие обоих атрибутов, мы получаем уникальный селектор

        browser.input1 = browser.find_element(By.CSS_SELECTOR,":required[class~='first']")
        browser.input1.send_keys("Dima")
        browser.input2 = browser.find_element(By.CSS_SELECTOR, ":required[class~='second']")
        browser.input2.send_keys("F")
        browser.input3 = browser.find_element(By.CSS_SELECTOR, ":required[class~='third']")
        browser.input3.send_keys("Msk")

    # Отправляем заполненную форму
        browser.button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(2)

    # находим элемент, содержащий текст
        browser.welcome_text_elt = browser.find_element(By.CLASS_NAME, "container")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        browser.welcome_text = browser.welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",browser.welcome_text, "Win!")

        browser.quit()

    def test_2(self,):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        # В тексте страницы, есть два поля, содержащих class="form-control second", но только у поля с фамилией так же имеется атрибут required, соответственно, сделав составной CSS селектор, учитываюший наличие обоих атрибутов, мы получаем уникальный селектор

        browser.input1 = browser.find_element(By.CSS_SELECTOR, ":required[class~='first']")
        browser.input1.send_keys("Dima")
        browser.input2 = browser.find_element(By.CSS_SELECTOR, ":required[class~='second']")
        browser.input2.send_keys("F")
        browser.input3 = browser.find_element(By.CSS_SELECTOR, ":required[class~='third']")
        browser.input3.send_keys("Msk")

        # Отправляем заполненную форму
        browser.button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        browser.welcome_text_elt = browser.find_element(By.CLASS_NAME, "container")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        browser.welcome_text = browser.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",browser.welcome_text, "Win!")
        browser.quit()


if __name__ == "__main__":
    unittest.main()









browser.implicitly_wait(5)