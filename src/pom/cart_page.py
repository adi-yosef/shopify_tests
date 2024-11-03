from .up_menu_page import UpMenuPage
from playwright.sync_api import expect


class CartPage(UpMenuPage):
    def __init__(self, page):
        super().__init__(page)

        self.check_out_button = page.get_by_role("button", name="Check out")

        #verify
        self.amount_total_33 = page.get_by_text("£33.00 GBP")
        self.cart_page_verify = page.get_by_role("heading", name="Your cart")

    def click_on_check_out_button(self):
        self.check_out_button.click()
        print("Click on checkout button")

    def verify_we_on_cart_page(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.cart_page_verify).to_be_visible()
        print("We are on the right page")


