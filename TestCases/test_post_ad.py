import time
from TestCases.BaseTest import BaseTest
from Pages.dashboard_page import DashboardPage


class Test_BareeGaree(BaseTest):
    def test_add_post(self):
        db = DashboardPage(self.driver)
        db.login_to_application()
        time.sleep(10)
        db.click_on_post_ad_button()
        db.click_on_sell_rent_button()
        db.click_on_electronics()
        time.sleep(5)
        db.click_on_laptops_button()
        time.sleep(5)
        db.enter_title()
        db.click_on_condition()
        db.click_on_brand()
        db.enter_model_name()
        db.enter_display_sixe()
        db.enter_ram()
        db.enter_processor()
        db.enter_hDD()
        db.enter_price()
        time.sleep(2)
        db.click_on_district()
        time.sleep(1)
        db.click_on_area()
        time.sleep(1)
        db.enter_phone_number()
        db.upload_image()
        db.click_on_submit()
        time.sleep(10)


