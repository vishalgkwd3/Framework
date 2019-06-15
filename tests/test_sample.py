from common_base.Seleniumbase import SeleniumBase
import common_base.logging_base as log

sb= SeleniumBase()

class TestSample:


        # naukri scenario to verify title
    def test_1(self):
        log.logger.error('in test 1')
        sb.launch_browser_app('chrome', 'https://www.naukri.com/')
        actual_title = sb.get_page_details('title')
        sb.compare_result('', actual_title)
        sb.close_browser()

    # naukri scenario to verify url
    def test_2(self):
        sb.launch_browser_app('chrome', 'https://www.naukri.com/')
        actual_url = sb.get_page_details('currenturl')
        sb.compare_result('', actual_url)
        sb.close_browser()

    def test_3(self):
        sb.launch_browser_app('chrome', 'https://www.naukri.com/')
        actual_title = sb.get_page_details('title')
        sb.compare_result('', actual_title)

        element = sb.get_element('name', 'q')
        element.send_keys('inportia')

        element = sb.get_element('name', 'btnK')
        element.submit()

        elements = sb.get_elements('partial link', 'inportia')
        sb.compare_result(str(9), str(len(elements))
                       )
        sb.close_browser()

    # Open facebook
    def test_4(self):
        sb.launch_browser_app('chrome', 'https://www.facebook.com/')
        actual_title = sb.get_page_details('title')
        sb.compare_result('', actual_title)

        element = sb.get_element('id', 'email')
        element.send_keys('vishalgkwd3@gmail.com')

        element = sb.get_element('id', 'pass')
        element.send_keys('december1992')

        element = sb.get_element('xpath', "//input[@value = 'Log In' ]")
        element.submit()

        exp_url = "https://www.facebook.com/"
        act_url = sb.get_page_details('currenturl')
        sb.compare_result(exp_url, act_url)

        sb.close_browser()

    # def scenario_5():
    #     expected_title = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    #     launch_browser_app('chrome', 'https://www.amazon.in/')
    #     actual_title = get_page_details('title')
    #     compare_result(expected_title, actual_title)
    #
    #     element = get_element('id', 'searchDropdownBox')
    #     # print(element.is_displayed())
    #     # print(element.is_enabled())
    #
    #     sel = Select(element)
    #     sel.select_by_value('search-alias=amazon-devices')
    #     sel.select_by_index(4)
    #     sel.select_by_visible_text('Baby')
    #
    #     element = get_element('xpath', "//span[@class='nav-search-label']")
    #
    #     compare_result('Baby', element.text)
    #
    #     close_browser()

    # Topic: Work on Dropdown & select dropdown

    def test_5(self):
        expected_title = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        sb.launch_browser_app('chrome', 'https://www.amazon.in/')
        actual_title = sb.get_page_details('title')
        sb.compare_result(expected_title, actual_title)

        element = sb.get_element('id', 'searchDropdownBox')
        # print(element.is_displayed())
        # print(element.is_enabled())

        sb.perform_action_on_element(element, 'select', 'Baby', extra='visibletext')

        element = sb.get_element('xpath', "//span[@class='nav-search-label']")

        actual_text = sb.perform_action_on_element(element, 'gettext')

        sb.compare_result('Baby', actual_text)

        sb.close_browser()

    # Topic: Switch to windows

    def test_6(self):

        expected_title = 'Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com'
        sb.launch_browser_app('chrome', 'https://www.naukri.com/')
        actual_title = sb.get_page_details('title')
        sb.compare_result(expected_title, actual_title)

        # print(get_page_details('handle'))
        # print(driver.window_handles)
        # print(len(driver.window_handles))

        sb.switch_to_another_object('window', 'Amazon')

        sb.close_browser()

    # Topic: Switch to frame

    def test_7(self):

        expected_title = 'The Internet'
        sb.launch_browser_app('chrome', 'https://the-internet.herokuapp.com/iframe')
        actual_title = sb.get_page_details('title')
        sb.compare_result(expected_title, actual_title)

        element = sb.get_element('id', 'mce_0_ifr')
        sb.switch_to_another_object('frame', element)

        element = sb.get_element('id', 'tinymce')
        sb.perform_action_on_element(element, 'settext', 'Vishal Gaikwad')

        sb.close_browser()

    # Topic: Switch to alert

    def test_8(self):
        expected_title = 'The Internet'
        sb.launch_browser_app('chrome', 'https://the-internet.herokuapp.com/javascript_alerts')
        actual_title = sb.get_page_details('title')
        sb.compare_result(expected_title, actual_title)

        element = sb.get_element('xpath', "//button[contains(text(), 'Click for JS Confirm')]")
        sb.perform_action_on_element(element, 'click')
        sb.switch_to_another_object('alert', 'accept')

        element = sb.get_element('id', 'result')
        actual = sb.perform_action_on_element(element, 'gettext')
        sb.compare_result('You clicked: Ok', actual)
        sb.close_browser()

    # Select many options form dropdown
    def test_9(self):
        expected_title = 'The Internet'
        sb.launch_browser_app('chrome', 'https://the-internet.herokuapp.com/javascript_alerts')
        actual_title = sb.get_page_details('title')
        sb.compare_result(expected_title, actual_title)