from pages.base_page import BasePage


class SearchPage(BasePage):
    def get_text_box_data(self):
        return self.base_selenium.get_value(element='search:box')

    def search_text(self, text, submit=False):
        self.base_selenium.set_text(element='search:box', value=text)
        if submit:
            self.base_selenium.click(element='search:google_search')

    def get_suggestions_data_list(self):
        return self.base_selenium.get_text(element='search:suggestions').split('\n')

    def inurl_search(self, text):
        data = 'inurl:{}'.format(text)
        self.search_text(data, submit=True)

