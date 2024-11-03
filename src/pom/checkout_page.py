from .up_menu_page import UpMenuPage
from playwright.sync_api import Page, Locator, expect

class CheckoutPage(UpMenuPage):
    def __init__(self, page):
        super().__init__(page)

        self.cost_summary = page.get_by_label("Cost summary").get_by_text("£56.99")
        self.email_phone_box = page.get_by_placeholder("Email or mobile phone number")
        self.phone_country_select = page.locator("select[name=\"phone_country_select\"]")

        self.last_name = page.get_by_placeholder("Last name")
        self.address = page.get_by_placeholder("Address")
        self.city = page.get_by_placeholder("City")
        self.pay_now_button = page.get_by_role("button", name="Pay now")

        #verify
        self.error_email_message = page.get_by_text("Enter a valid email")
        self.order_confirmed = page.get_by_role("heading", name="Your order is confirmed")

        self.card_number_input = self.page.frame_locator("iframe.card-fields-iframe").nth(0).locator("input[placeholder='Card number']")
        self.expiration_date_input = self.page.frame_locator("iframe.card-fields-iframe").nth(1).locator("input[placeholder='Expiration date (MM / YY)']")
        self.security_code_input = self.page.frame_locator("iframe.card-fields-iframe").nth(2).locator("input[placeholder='Security code']")
        self.name_on_card_input = self.page.frame_locator("iframe.card-fields-iframe").nth(5).locator("input[placeholder='Name on card']")


    def fill_email_phone_box(self, string: str):
        self.email_phone_box.fill(string)

    def choose_country(self, string: str):
        self.phone_country_select.select_option(string)

    def fill_last_name(self, string: str):
        self.last_name.fill(string)

    def fill_address(self, string: str):
        self.address.fill(string)

    def fill_city(self, string: str):
        self.city.fill(string)

    def click_on_pay_now(self):
        self.pay_now_button.click()

    def wait_for_page_idle(self):
        self.page.wait_for_load_state("networkidle")

    def fill_card_number(self, card_number: str):
        self.card_number_input.fill(card_number)

    def fill_card_details(
            self,
            card_number: str,
            expiration_date:str,
            security_code: str,
            name: str
    ) -> None:
        self.card_number_input.fill(card_number)
        self.expiration_date_input.fill(expiration_date)
        self.security_code_input.fill(security_code)
        self.name_on_card_input.fill(name)

    def fill_form_details(
            self,
            phone_or_email: str,
            country: str,
            last_name: str,
            address: str,
            city: str
    ) -> None:
        self.fill_email_phone_box(phone_or_email)
        self.choose_country(country)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_city(city)

    def check_header_color(self):
        header = self.page.query_selector('header[role="banner"]')
        header_color = header.evaluate("header => getComputedStyle(header).color")
        print(f"Header color: {header_color}")
        expected_color = 'rgb(255, 0, 0)'
        expect(header_color).to_be(expected_color, f"Expected header color to be {expected_color}, but got {header_color}")