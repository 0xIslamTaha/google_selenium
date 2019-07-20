from pages.base_page import BasePage


class ResultsPage(BasePage):
    def get_results_urls(self):
        results_class = self.base_selenium.find_element(element="search_results:results")
        results = [result.find_element_by_tag_name('a').get_attribute('href') for result in results_class]
        return results
