from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]/i'
    filtered_usernames = '(//div[@Class="list-container"] //tr //td)[2]'
    filtered_user_roles = '(//div[@Class="list-container"] //tr //td)[3]'
    filter_no_records_message = '//div[text()="No Records Found"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_user(self):
        self.step.click_on_element(self.add_user_button)

    def click_filter_button(self):
        self.step.click_on_element(self.filter_users_button)

    def get_filtered_usernames(self):
        return self.step.get_elements_texts(self.filtered_usernames)

    def get_filtered_user_role(self):
        return self.step.get_elements_texts(self.filtered_user_roles)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message, 2)
        return self.step.get_element_text(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        if not self.step.specified_element_is_present(self.filtered_usernames):
            return True
        else:
            elements = self.step.get_list_of_elements(self.filtered_usernames)
            if not elements:
                return True
            else:
                return False