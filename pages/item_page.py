from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.item_stars_count_in_item_page = (By.CSS_SELECTOR, "[class='fave-count-label']")
        self.item_comments_count_in_item_page = (By.CSS_SELECTOR, "[class='comment-count-label']")
        self.item_user_and_galleryin_item_page = (By.CSS_SELECTOR, "[class='sub-photo-content-container']")

    def get_item_user_and_gallery_in_item_page(self):
        return self.get_text(self.item_user_and_galleryin_item_page)

    def get_item_comments_count_in_item_page(self):
        return self.get_text(self.item_comments_count_in_item_page)


    def get_item_stars_count_in_item_page(self):
        return self.get_text(self.item_stars_count_in_item_page)
