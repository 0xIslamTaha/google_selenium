from testcases.base_tests import BaseTest
from parameterized import parameterized


class TextSearch(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url(url=self.url)

    def test001_search_text_box_is_editable(self):
        """
        TC001: Verify that text box is editable.
            1- Get http://google.com
            2- Get data from text box, should be empty
            3- Set keyword in text box
            4- Verify that text box has this keyword"
        """
        self.base_selenium.LOGGER.info('Get data from text box, should be empty.')
        self.assertFalse(self.search_page.get_text_box_data(), "Text box should be empty.")

        random_text = self.generate_random_text()
        self.base_selenium.LOGGER.info('Set {} keyword in text box.'.format(random_text))
        self.search_page.search_text(text=random_text)

        self.base_selenium.LOGGER.info('Assert text box has {} value.'.format(random_text))
        self.assertEqual(random_text, self.search_page.get_text_box_data(),
                         "Text box should have {} value.".format(random_text))

    @parameterized.expand(["face", "yahoo"])
    def test004_auto_suggestions(self, word):
        """
        TC004: Verify that auto-suggestions features returns correct results

        1- Get http://google.com
        2- Set {} keyword
        3- Verify that there is {} in suggestions list"
        """.format(word, word)

        self.base_selenium.LOGGER.info('Set {} keyword'.format(word))
        self.search_page.search_text(text=word)

        self.base_selenium.LOGGER.info('Assert {} in suggestions list'.format(word))
        for data in self.search_page.get_suggestions_data_list():
            self.assertIn(word, data)

    @parameterized.expand(['0xislamtaha'])
    def test006_inurl_feature(self, word):
        """"
         TC006: Verify that auto-suggestions features returns correct results

        1- Get http://google.com
        2- search for any word with "inurl:" feature
        3- Verify that all results url has this keyword
        """
        self.base_selenium.LOGGER.info('search for "inurl:{}" feature'.format(word))
        self.search_page.inurl_search(text=word)

        self.base_selenium.LOGGER.info('Verify that all results url has {}'.format(word))
        for result in self.results_page.get_results_urls():
            self.base_selenium.LOGGER.info('assert {} in {}'.format(word.lower(), result.lower()))
            self.assertIn(word.lower(), result.lower())
