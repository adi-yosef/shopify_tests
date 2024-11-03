import pytest
from playwright.sync_api import expect
from src.steps.search_item import search_item_and_click_on_it

@pytest.mark.ui
@pytest.mark.sad_flow
def test_negative(
        up_menu_page,
        dropit_hamburger_page,
        dropit_chips_page,
        cart_page,
        checkout_page

) -> None:
    search_item_and_click_on_it("Dropit Hamburger (QA Automation)", "Dropit Hamburger (QA Automation)", dropit_hamburger_page.page)
    dropit_hamburger_page.add_burger_to_cart("1", "large")
    search_item_and_click_on_it("Dropit Chips (QA Automation)", "Dropit Chips (QA Automation)", dropit_chips_page.page)
    dropit_chips_page.add_chips_to_cart("1", "medium")
    up_menu_page.click_on_cart_link()
    # need to check on cart page
    cart_page.click_on_check_out_button()
    checkout_page.wait_for_page_idle()
    expect(checkout_page.pay_now_button).to_be_visible()
    checkout_page.fill_email_phone_box("non_valid")
    checkout_page.click_on_pay_now()
    expect(checkout_page.error_email_message).to_be_visible()

    # checkout_page.check_header_color()
    # header is not red
    checkout_page.fill_card_number("1234")
    checkout_page.click_on_pay_now()
    expect(checkout_page.error_email_message).to_be_visible()



