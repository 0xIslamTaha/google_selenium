from unittest import TestCase
from framework.base_selenium import BaseSelenium
from pages.search_page import SearchPage
from pages.results_page import ResultsPage
from testconfig import config
from uuid import uuid4


class BaseTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_selenium = BaseSelenium()
        self.search_page = SearchPage()
        self.results_page = ResultsPage()

    def setUp(self):
        print('\t')
        self.base_selenium.LOGGER.info('Test case : {}'.format(self._testMethodName))
        self.base_selenium.get_driver()
        self.url = config['site']['url']

    def tearDown(self):
        self.base_selenium.quit_driver()
        self.base_selenium.LOGGER.info('TearDown. \t')

    @staticmethod
    def generate_random_text():
        return str(uuid4()).replace("-", "")[:10]

