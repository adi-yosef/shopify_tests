from playwright.sync_api import Page

from .up_menu_page import UpMenuPage


class HomePage(UpMenuPage):
    def __init__(self, page: Page):
        super().__init__(page)
       # self.shop_all_link = page.get_by_role("link", name="Shop all")