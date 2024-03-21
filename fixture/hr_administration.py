from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]/i'
    filtered_username = '//span[text()="admin"]'
    filtered_user_role = '//span[text()="Global Admin"]'
    filter_no_records_message = '//div[text()="No Records Found"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_user(self):
        self.step.click_on_element(self.add_user_button)

    def click_filter_button(self):
        self.step.click_on_element(self.filter_users_button)

    def get_filtered_username(self):
        return self.step.get_element_text(self.filtered_username)

    def get_filtered_user_role(self):
        return self.step.get_element_text(self.filtered_user_role)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message, 2)
        return self.step.get_element_text(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filtered_username)