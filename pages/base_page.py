from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Метод открывает нужную страницу используя метод get()"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Метод проверяет наличие элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
