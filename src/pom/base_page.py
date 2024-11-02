
class BasePage:
    def __init__(self, page) -> None:
        self.page = page


        self.home_link = page.get_by_role("link", name="Home")
        self.catalog_link = page.get_by_role("link", name="Catalog")
        self.contact_link = page.get_by_role("link", name="Contact")
        self.search_button = page.get_by_role("button", name="Search")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.shop_all_link = page.get_by_role("link", name="Shop all")


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

    def click_on_shop_all_link(self):
        self.shop_all_link.click()


