from pages.home_page import HomePage
from pages.login_page import LoginPage
from params.parameters import TestParams
from tests.base_test import BaseTest

class TestHomePage(BaseTest):
    ITEMS_TO_SCAN = 20

    def test_orientation_filter(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.open_advance_filer_for_tag(TestParams.TAG_TO_SEARCH)

        home.set_landscape_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < self.ITEMS_TO_SCAN:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width > height
                count += 1
            else:
                break

    def test_portrait_filter(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.open_advance_filer_for_tag(TestParams.TAG_TO_SEARCH)

        # test portrait orientation filter
        home.set_portrait_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < self.ITEMS_TO_SCAN:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width < height
                count += 1
            else:
                break

    def test_square_filter(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.open_advance_filer_for_tag(TestParams.TAG_TO_SEARCH)

        # test square orientation filter
        home.set_square_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < self.ITEMS_TO_SCAN:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width < height + 2 and height < width + 2
                count += 1
            else:
                break

    def test_panorama_filter(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.open_advance_filer_for_tag(TestParams.TAG_TO_SEARCH)

        # test panorama orientation filter
        home.set_panorama_filter()
        items = home.get_items()
        count = 1
        for item in items:
            if count < self.ITEMS_TO_SCAN:
                print(f"count: {count}")
                width = home.get_item_style_num(item, style_part=4)
                height = home.get_item_style_num(item, style_part=6)
                assert width > height * 2
                count += 1
            else:
                break