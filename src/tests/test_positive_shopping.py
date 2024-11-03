import pytest
from playwright.sync_api import expect
from src.steps.search_item import search_item_and_click_on_it

@pytest.mark.ui
@pytest.mark.happy_flow
def test_positive(
        up_menu_page,
        dropit_hamburger_page,
        dropit_chips_page,
        cart_page,
        checkout_page

) -> None:
    search_item_and_click_on_it("Dropit Hamburger (QA Automation)", "Dropit Hamburger (QA Automation)", dropit_hamburger_page.page)
    dropit_hamburger_page.add_burger_to_cart("2", "medium")
    dropit_hamburger_page.add_burger_to_cart("1", "so_large")
    search_item_and_click_on_it("Dropit Chips (QA Automation)", "Dropit Chips (QA Automation)", dropit_chips_page.page)
    dropit_chips_page.add_chips_to_cart("2", "large")
    dropit_chips_page.add_chips_to_cart("1", "too_much")
    expect(up_menu_page.cart_link_6_items).to_be_visible()
    dropit_chips_page.click_on_cart_link_6_items()
    expect(cart_page.amount_total_33).to_be_visible()
    cart_page.click_on_check_out_button()
    checkout_page.wait_for_page_idle()
    expect(checkout_page.cost_summary).to_be_visible()

    checkout_page.fill_form_details("0544608611", "IL", "El Toro", "The Moon", "The crater on the left")
    checkout_page.fill_card_details("1","12/26","777","Bogus Gateway")
    checkout_page.click_on_pay_now()
    expect(checkout_page.order_confirmed).to_be_visible()

