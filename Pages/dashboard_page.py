import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Config.config import TestData
from Pages.BasePage import BasePage
from Locators.Locators import Locators


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def login_to_application(self):
        try:
            self.click_element(self.locator.dialogOk)
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("Dialog Box is not present on the website")
        self.click_element(self.locator.loginDropdown)
        self.click_element(self.locator.generalUser)
        self.enter_at(self.locator.email, TestData.USER_NAME)
        self.enter_at(self.locator.password, TestData.PASSWORD)
        self.click_element(self.locator.buttonLogin)

    def click_on_post_ad_button(self):
        self.click_element(self.locator.postAd)

    def click_on_sell_rent_button(self):
        self.click_element(self.locator.sellRentButton)

    def click_on_electronics(self):
        self.click_element(self.locator.electronics)

    def click_on_laptops_button(self):
        self.click_element(self.locator.laptops)

    def enter_title(self):
        self.enter_at(self.locator.title, "LAPTOP")

    def click_on_condition(self):
        self.click_element(self.locator.condition1)
        self.enter_at(self.locator.searchCondition, "New")
        time.sleep(1)
        self.click_element(self.locator.new)

    def click_on_brand(self):
        self.click_element(self.locator.brand1)
        self.enter_at(self.locator.searchCondition, "HP")
        time.sleep(1)
        self.click_element(self.locator.hp)

    def enter_model_name(self):
        self.enter_at(self.locator.model, "HP Probook 450 G4")

    def enter_display_sixe(self):
        self.enter_at(self.locator.displaySize, "14\"")

    def enter_ram(self):
        self.enter_at(self.locator.ram, "8 GB")

    def enter_processor(self):
        self.enter_at(self.locator.processor, "core i7, 11 Generation")

    def enter_hDD(self):
        self.enter_at(self.locator.hDD, "1 TB")

    def enter_price(self):
        self.enter_at(self.locator.price, "50000")

    def click_on_district(self):
        select = Select(self.get_element(self.locator.district))
        select.select_by_value("1")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(self.locator.district));
        # self.click_element(self.locator.district)
        # self.enter_at(self.locator.searchCondition, "Dhaka")
        # time.sleep(1)
        # self.click_element(self.locator.dhaka)

    def click_on_area(self):
        select = Select(self.get_element(self.locator.area))
        select.select_by_value("50")
        # self.click_element(self.locator.area)
        # self.enter_at(self.locator.searchCondition, "Aftab Nagar")
        # time.sleep(1)
        # self.click_element(self.locator.aftagNagar)

    def enter_phone_number(self):
        self.enter_at(self.locator.phoneNumber, "01712122436")

    def upload_image(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "images/HPProbook.jpg"))
        file_input = self.driver.find_element(By.ID, self.locator.image)
        file_input.send_keys(upload_file)

    def click_on_submit(self):
        self.click_element(self.locator.submit)
