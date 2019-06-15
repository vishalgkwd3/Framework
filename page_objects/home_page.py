from common_base.base import Base


xpath_home_tabs = "//ul[@class = 'midSec menu']/li"

class HomePage(Base):

    def get_tab_elements(self):
        return self.get_elements('xpath', xpath_home_tabs)

    def get_tab_count(self):
        return len(self.get_tab_elements())

    def get_tab_text(self):
        elements = self.get_tab_elements()
        tab_text = []

        for element in elements:
            tab_name = self.perform_action_on_element(element, action_type='gettext')
            tab_text.append(tab_name)
        # print(tab_text)
        return tab_text

    def get_window_count(self):
        return len(self.get_page_details('handles'))



