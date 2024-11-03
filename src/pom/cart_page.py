from .up_menu_page import UpMenuPage


class CartPage(UpMenuPage):
    def __init__(self, page):
        super().__init__(page)

        self.check_out_button = page.get_by_role("button", name="Check out")


        self.amount_total_33 = page.get_by_text("£33.00 GBP")

    def click_on_check_out_button(self):
        self.check_out_button.click()
        print("Click on checkout button")


