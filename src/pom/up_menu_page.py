from playwright.sync_api import Page, expect


class UpMenuPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.home_link = page.get_by_role("link", name="Home")
        self.catalog_link = page.get_by_role("link", name="Catalog")
        self.contact_link = page.get_by_role("link", name="Contact")

        self.search_button = page.get_by_role("button", name="Search")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.search_box = page.get_by_placeholder("Search")

        #verify
        self.cart_link_6_items = page.get_by_role("link", name="Cart 6 items")



    def click_on_home_link(self):
        self.home_link.click()

    def click_on_catalog_link(self):
        self.catalog_link.click()

    def click_on_contact_link(self):
        self.contact_link.click()

    def click_on_search_button(self):
        self.search_button.click()

    def click_on_cart_link(self):
        self.cart_link.click()

    def click_on_cart_link_6_items(self):
        self.cart_link_6_items.click()

    def fill_search_box(self, name: str):
        self.search_box.fill(name)
