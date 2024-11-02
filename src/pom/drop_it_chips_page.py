from .up_menu_page import UpMenuPage


class DropItChipsPage(UpMenuPage):
    def __init__(self, page):
        super().__init__(page)

        self.dropit_chips_headline = page.get_by_role("heading", name="Dropit Chips (QA Automation)")

        self.size_small = page.get_by_text("Small", exact=True)
        self.size_medium = page.get_by_text("Medium", exact=True)
        self.size_large = page.get_by_text("Large", exact=True)
        self.size_too_much = page.get_by_text("Too much for you to handle")

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

    def click_on_size_too_much(self):
        self.size_too_much.click()

    def fill_quantity(self, num: int):
        self.quantity.fill(num)

    def click_on_plus_quantity(self):
        self.plus_quantity.click()

    def click_on_minus_quantity(self):
        self.minus_quantity.click()

    def click_on_add_to_cart(self):
        self.add_to_cart.click()

    def click_on_continue_shopping(self):
        self.continue_shopping()


