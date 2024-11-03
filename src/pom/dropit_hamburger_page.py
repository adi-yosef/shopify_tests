from .up_menu_page import UpMenuPage


class DropItBurgerPage(UpMenuPage):
    def __init__(self, page):
        super().__init__(page)
        self.search_result =  page.get_by_role("link", name="Dropit Hamburger (QA")
        self.dropit_burger_headline = page.get_by_role("heading", name="Dropit Hamburger (QA")

        self.size_small = page.get_by_text("Small", exact=True)
        self.size_medium = page.get_by_text("Medium", exact=True)
        self.size_large = page.get_by_text("Large", exact=True)
        self.size_so_large = page.get_by_text("So large you can't eat it")

        self.quantity = page.get_by_label("Quantity")
        self.plus_quantity = page.get_by_role("button", name="Increase quantity for Dropit")
        self.minus_quantity = page.get_by_role("button", name="Decrease quantity for Dropit")

        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.buy_it_now = page.get_by_role("button", name="Buy it now")

        #popup
        self.continue_shopping = page.get_by_role("button", name="Continue shopping")

    def click_on_small_size(self):
        self.size_small.click()

    def click_on_medium_size(self):
        self.size_medium.click()

    def click_on_large_size(self):
        self.size_large.click()

    def click_on_size_so_large_size(self):
        self.size_so_large.click()

    def fill_quantity(self, num: str):
        self.quantity.fill(num)

    def click_on_plus_quantity(self):
        self.plus_quantity.click()

    def click_on_minus_quantity(self):
        self.minus_quantity.click()

    def click_on_add_to_cart(self):
        self.add_to_cart.click()

    def click_on_continue_shopping(self):
        self.continue_shopping.click()

    def click_on_search_result(self):
        self.search_result.click()


