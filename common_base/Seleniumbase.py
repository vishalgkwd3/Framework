#Selenium to check the browser title
# import selenium.webdriver as wdriver
#
# # expected_url = ''
# driver = wdriver.Chrome(executable_path='./drivers/chromedriver.exe')
# # driver.get('https://www.practicepython.org/')
#
# driver.get('https://www.naukri.com/')
# expected_title = 'Jobs - Recruitment -- Job Search - Employment - Job Vacancies - Naukri.com'
# driver.maximize_window()
# # driver.get(expected_url)
# actual_title = driver.title
#
# print(actual_title)
#
# actual_url = driver.current_url
# print(actual_url)
#
# # assert actual_url == expected_url, actual_url + ' is not matching with ' + expected_url
# assert expected_title == actual_title
# # driver.close()
# driver.quit()

import selenium.webdriver as wdriver
from selenium.webdriver.support.select import Select
import common_base.logging_base as log

class SeleniumBase():

    def __init__(self):
        self.driver = None


    # launch browser, maximise it & application
    def launch_browser_app(self,browser_name, url):

        if browser_name == 'chrome':
            self.driver = wdriver.Chrome(executable_path='./drivers/chromedriver.exe')
            log.logger.info(browser_name,'launched')

        self.driver.maximize_window()
        self.driver.get(url)

    # get the title for url
    def get_page_details(self,detail_type):

        if detail_type == 'title':
            return self.driver.title
        elif detail_type == 'currenturl':
            return self.driver.current_url
        elif detail_type == 'handle':
            return self.driver.current_window_handle
        elif detail_type == 'handles':
            return self.driver.window_handles

    def compare_result(self,expected_value, actual_value):
        # pass
        assert expected_value == actual_value, (actual_value , ' is not matching with ' , expected_value)

    def close_browser(self):
        self.driver.quit()

    def get_element(self,locator_type, value):

        if locator_type == 'id':
            return self.driver.find_element_by_id(value)
        elif locator_type == 'name':
            return self.driver.find_element_by_name(value)
        elif locator_type == 'classname':
            return self.driver.find_element_by_class_name(value)
        elif locator_type == 'tagname':
            return self.driver.find_element_by_tag_name(value)
        elif locator_type == ' linktext':
            return self.driver.find_element_by_link_text(value)
        elif locator_type == 'partial link':
            return self.driver.find_element_by_partial_link_text(value)
        elif locator_type == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif locator_type == 'CSS':
            return self.driver.find_element_by_css_selector(value)
        else:
            log.logger.debug('Invalid locator specified')

    def get_elements(self,locator_type, value):

        if locator_type == 'id':
            return self.driver.find_elements_by_id(value)
        elif locator_type == 'name':
            return self.driver.find_elements_by_name(value)
        elif locator_type == 'classname':
            return self.driver.find_elements_by_class_name(value)
        elif locator_type == 'tagname':
            return self.driver.find_elements_by_tag_name(value)
        elif locator_type == ' linktext':
            return self.driver.find_elements_by_link_text(value)
        elif locator_type == 'partial link':
            return self.driver.find_elements_by_partial_link_text(value)
        elif locator_type == 'xpath':
            return self.driver.find_elements_by_xpath(value)
        elif locator_type == 'CSS':
            return self.driver.find_elements_by_css_selector(value)
        else:
            log.logger.debug('Invalid locator specified')

    def perform_action_on_element(self,element, action_type, value=None, extra=None):

        return_value = None

        if action_type == 'click':
            element.click()
        elif action_type == 'settext':
            element.clear()
            element.send_keys(value)
        elif action_type == 'gettext':
            return_value = element.text
        elif action_type == 'select':
            sel = Select(element)
            if extra == 'visibletext':
                sel.select_by_visible_text(value)
            elif extra == 'index':
                sel.select_by_index(value)
            elif extra == 'value':  # this value is different
                sel.select_by_value()
            else:
                print(extra, 'is incorrect')
        else:
            print(action_type, 'is incorrect')

        return return_value

    def switch_to_another_object(self,obj_type, expected_value=None):

        if obj_type == 'window':
            main_handle = self.get_page_details('handle')
            all_handle = self.get_page_details('handles')

            for handle in all_handle:
                if handle != main_handle:
                    self.driver.switch_to.window(handle)
                    actual_title = self.get_page_details('title')
                    if actual_title == expected_value:
                        print(actual_title)
                        break
                    else:
                        continue

        elif obj_type == 'frame':
            self.driver.switch_to.frame(expected_value)
        elif obj_type == 'alert':
            alert = self.driver.switch_to.alert
            if expected_value == 'accept':
                alert.accept()
            elif expected_value == 'dismiss':
                alert.dismiss()
