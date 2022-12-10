from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from params.parameters import TestParams
from tests.base_test import BaseTest


class TestItemPage(BaseTest):
    def test_dava_validation(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        item_page = ItemPage(self.driver)
        login.perform_login(TestParams.USERNAME, TestParams.PASSWORD)
        home.search_tag(TestParams.TAG_TO_SEARCH)
        home.click_title_view()
        rand_item = home.get_random_item()
        item_title_in_gallery = rand_item.find_element(By.CSS_SELECTOR, "[class='metadata']>:nth-child(1)").text
        item_user_in_gallery = rand_item.find_element(By.CSS_SELECTOR, " [class='metadata']>:nth-child(2)").text.replace(
            "by ", "")
        item_stars_count_in_gallery = rand_item.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(1)").text
        item_comments_count_in_gallery = rand_item.find_element(By.CSS_SELECTOR, "[class='engagement']>:nth-child(2)").text
        rand_item.find_element(By.CSS_SELECTOR, "a").click()
        item_stars_count_in_item_page = item_page.get_item_stars_count_in_item_page()
        item_comments_count_in_item_page = item_page.get_item_comments_count_in_item_page()
        item_user_and_galleryin_item_page = item_page.get_item_user_and_gallery_in_item_page()

        assert item_stars_count_in_gallery == item_stars_count_in_item_page
        assert item_comments_count_in_gallery == item_comments_count_in_item_page
        assert item_title_in_gallery in item_user_and_galleryin_item_page
        assert item_user_in_gallery in item_user_and_galleryin_item_page
