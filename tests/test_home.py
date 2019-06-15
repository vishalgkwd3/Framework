import sys
import pytest
from page_objects.home_page import HomePage

hp = HomePage()

class TestHomePage:

    @pytest.fixture
    def initial_setup(self):
        test_data = hp.get_section_data_from_ini_file('common.ini', 'common')
        hp.launch_browser_app(test_data['browser_name'], test_data['url'])
        actual_title = hp.get_page_details('title')
        hp.compare_result(actual_title, test_data['expected_title'])

    def test_verify_tab_count(self, initial_setup):
        this_function_name = sys._getframe().f_code.co_name
        test_data = hp.get_section_data_from_ini_file('home_data.ini',this_function_name)
        actual_tab_count = hp.get_tab_count()
        hp.compare_result(actual_tab_count, int(test_data['expected_tab_count']))
        hp.close_browser()


    def test_verify_tab_text(self, initial_setup):
        this_function_name = sys._getframe().f_code.co_name
        test_data = hp.get_section_data_from_ini_file('home_data.ini',this_function_name)
        actual_tab_name = hp.get_tab_text()
        hp.compare_result(actual_tab_name, test_data['expected_tab_name'].split(','))
        hp.close_browser()

    def test_verify_window_count(self, initial_setup):
        this_function_name = sys._getframe().f_code.co_name
        test_data = hp.get_section_data_from_ini_file('home_data.ini', this_function_name)
        actual_window_count = hp.get_window_count()
        hp.compare_result(int(actual_window_count), int(test_data['expected_window_count']))
