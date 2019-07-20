from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from elements import elements
import time
from loguru import logger


class BaseSelenium:
    TIME_TINY = 2
    TIME_SMALL = 5
    TIME_MEDIUM = 10
    TIME_LARGE = 15
    TIME_X_LARGE = 60

    IMPLICITLY_WAIT = 60
    EXPLICITLY_WAIT = 120

    LOGGER = logger
    LOGGER.add('log_{time}.log', backtrace=False)

    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.elements = elements

    def get_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(BaseSelenium.IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, BaseSelenium.EXPLICITLY_WAIT)

    def quit_driver(self):
        self.driver.quit()

    def _get_method_value_order(self, element):
        element_page, element_name = element.split(':')
        method = self.elements[element_page][element_name]['method'].upper()
        value = self.elements[element_page][element_name]['value']
        if 'order' in self.elements[element_page][element_name]:
            order = self.elements[element_page][element_name]['order']
        else:
            order = None
        return method, value, order

    def _wait_until_element_located(self, element):
        method, value, order = self._get_method_value_order(element=element)
        if order == 0:
            return self.wait.until(EC.visibility_of_element_located((getattr(By, method), value)))
        else:
            dom_element = self.find_element(element=element)
            end_time = time.time() + BaseSelenium.EXPLICITLY_WAIT
            while True:
                if dom_element.is_displayed():
                    return dom_element
                else:
                    time.sleep(0.5)
                if time.time() > end_time:
                    break
            raise TimeoutException()

    def _wait_until_element_clickable(self, element):
        method, value, order = self._get_method_value_order(element=element)
        if order == 0:
            return self.wait.until(EC.element_to_be_clickable((getattr(By, method), value)))
        else:
            dom_element = self.find_element(element=element)
            end_time = time.time() + BaseSelenium.EXPLICITLY_WAIT
            while True:
                if dom_element.is_displayed() and dom_element.is_enabled():
                    return dom_element
                else:
                    time.sleep(0.5)
                if time.time() > end_time:
                    break
            raise TimeoutException()

    def find_element(self, element):
        method, value, order = self._get_method_value_order(element=element)
        if method in ['XPATH', 'ID', 'LINK_TEXT', 'CSS_SELECTOR']:
            element_value = self.driver.find_element(getattr(By, method), value)
        elif method in ['CLASS_NAME', 'NAME', 'TAG_NAME']:
            elements_value = self.driver.find_elements(getattr(By, method), value)
            if order == -1:
                element_value = elements_value
            else:
                element_value = elements_value[order]
        else:
            self.LOGGER.error(" This %s method isn't defined" % method)
            raise BaseException
        return element_value

    def get_text(self, element):
        self._wait_until_element_located(element)
        return self.find_element(element).text

    def set_text(self, element, value):
        self._wait_until_element_located(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(value)

    def clear_text(self, element):
        self._wait_until_element_located(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(Keys.ENTER)

    def click(self, element):
        dom_element = self._wait_until_element_clickable(element=element)
        dom_element.click()

    def get_url(self, url):
        self.LOGGER.info(" Get {} URL.".format(url))
        self.driver.get(url)

    def get_attribute(self, element, attribute):
        self._wait_until_element_located(element)
        return self.find_element(element).get_attribute(attribute)

    def get_value(self, element):
        return self.get_attribute(element, "value")
