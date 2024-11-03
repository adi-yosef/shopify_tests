import pytest
from playwright.sync_api import expect
from src.steps.search_item import search_item_and_click_on_it

@pytest.mark.ui
def test_positive(
        up_menu_page,
        dropit_hamburger_page,
        dropit_chips_page,
        cart_page,
        checkout_page

) -> None:
    search_item_and_click_on_it("Dropit Hamburger (QA Automation)", "Dropit Hamburger (QA Automation)", dropit_hamburger_page.page)
    dropit_hamburger_page.fill_quantity("2")
    dropit_hamburger_page.click_on_medium_size()
    dropit_hamburger_page.click_on_add_to_cart()
    dropit_hamburger_page.click_on_continue_shopping()
    dropit_hamburger_page.fill_quantity("1")
    dropit_hamburger_page.click_on_size_so_large_size()
    dropit_hamburger_page.click_on_add_to_cart()
    dropit_hamburger_page.click_on_continue_shopping()

    search_item_and_click_on_it("Dropit Chips (QA Automation)", "Dropit Chips (QA Automation)", dropit_chips_page.page)
    dropit_chips_page.fill_quantity("2")
    dropit_chips_page.click_on_large_size()
    dropit_chips_page.click_on_add_to_cart()
    dropit_chips_page.click_on_continue_shopping()
    dropit_chips_page.fill_quantity("1")
    dropit_chips_page.click_on_size_too_much()
    dropit_chips_page.click_on_add_to_cart()
    dropit_chips_page.click_on_continue_shopping()

    expect(up_menu_page.cart_link_6_items).to_be_visible()
    dropit_chips_page.click_on_cart_link_6_items()
    expect(cart_page.amount_total_33).to_be_visible()
    cart_page.click_on_check_out_button()
    checkout_page.wait_for_page_idle()
    expect(checkout_page.cost_summary).to_be_visible()
    checkout_page.fill_email_phone_box("0544608611")
    checkout_page.choose_country("IL")
    checkout_page.fill_last_name("El Toro")
    checkout_page.fill_address("The Moon")
    checkout_page.fill_city("The crater on the left")
    checkout_page.fill_card_details("1","12/26","777","Bogus Gateway")
    checkout_page.click_on_pay_now()
    expect(checkout_page.order_confirmed).to_be_visible()

