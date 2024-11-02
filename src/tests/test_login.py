import pytest

#import re
from playwright.sync_api import Page, expect
from src.tests.conftest import *
from src.steps.search_item import search_item_and_click_on_it



def test_positive(
        up_menu_page,
        dropit_hamburger_page,
        dropit_chips_page,
        cart_page
) -> None:
    search_item_and_click_on_it("Dropit Chips (QA Automation)","Dropit Hamburger (QA", up_menu_page)
    dropit_hamburger_page.fill_quantity(2)
    dropit_hamburger_page.click_on_medium_size()
    dropit_hamburger_page.click_on_add_to_cart()
    dropit_hamburger_page.click_on_continue_shopping()
    dropit_hamburger_page.fill_quantity(1)
    dropit_hamburger_page.click_on_size_so_large_size()
    dropit_hamburger_page.click_on_add_to_cart()
    dropit_hamburger_page.click_on_continue_shopping()

    search_item_and_click_on_it("Dropit Chips (QA Automation)", dropit_chips_page)
    dropit_chips_page.fill_quantity(2)
    dropit_chips_page.click_on_large_size()
    dropit_chips_page.click_on_add_to_cart()
    dropit_chips_page.click_on_continue_shopping()
    dropit_chips_page.fill_quantity(1)
    dropit_chips_page.click_on_size_too_much()
    dropit_chips_page.click_on_add_to_cart()
    dropit_chips_page.click_on_continue_shopping()

    expect(up_menu_page.cart_link_6_items.to_be_visible())
    dropit_chips_page.click_on_cart_link_6_items()

    cart_page.click_on_check_out_button()
    expect(cart_page.amount_total_33.to_be_visible())
    pass

    expect(page.get_by_role("strong")).to_contain_text("£56.99")
    page.get_by_placeholder("Email or mobile phone number").click()
    page.get_by_placeholder("Email or mobile phone number").fill("1800987654321")
    page.locator("iframe[name=\"card-fields-number-pf3m0i4jnfp00000\"]").content_frame.get_by_placeholder("Card number").click()
    page.locator("iframe[name=\"card-fields-number-pf3m0i4jnfp00000\"]").content_frame.get_by_placeholder("Card number").fill("1")
    page.locator("iframe[name=\"card-fields-expiry-4vy96wtiuwh00000\"]").content_frame.get_by_placeholder("Expiration date (MM / YY)").click()
    page.locator("iframe[name=\"card-fields-expiry-4vy96wtiuwh00000\"]").content_frame.get_by_placeholder("Expiration date (MM / YY)").click()
    page.locator("iframe[name=\"card-fields-expiry-4vy96wtiuwh00000\"]").content_frame.get_by_placeholder("Expiration date (MM / YY)").fill("12 / 26")
    page.locator("iframe[name=\"card-fields-expiry-4vy96wtiuwh00000\"]").content_frame.get_by_placeholder("Expiration date (MM / YY)").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_placeholder("Security code").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_placeholder("Security code").fill("777")
    page.locator("iframe[name=\"card-fields-name-p2lpfqcxres00000\"]").content_frame.get_by_placeholder("Name on card").click()
    page.locator("iframe[name=\"card-fields-name-p2lpfqcxres00000\"]").content_frame.get_by_placeholder("Name on card").fill("Bogus Gateway")
    page.get_by_placeholder("Email or mobile phone number").click()
    page.get_by_placeholder("Email or mobile phone number").fill("180098765432")
    page.locator("._9F1Rf").click()
    page.get_by_role("button", name="Pay now").click()
    page.get_by_placeholder("Last name").fill("el toro")
    page.get_by_placeholder("Address").click()
    page.get_by_placeholder("Address").fill("The moon")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("the crater to the left")
    page.get_by_role("button", name="Pay now").click()
    page.locator(".gdtca").click(button="right")
    page.get_by_role("button", name="Pay now").click()
    page.get_by_label("Bogus Last four digits").click()
    page.get_by_label("Bogus Last four digits").click()
    page.locator("div").filter(has_text=re.compile(r"^Credit card$")).nth(1).click()
    page.get_by_label("Use shipping address as").uncheck()
    page.get_by_label("Use shipping address as").check()
    page.get_by_role("button", name="Delete card").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").click(button="right")
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").fill("777777\\")
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").click()
    page.locator("iframe[name=\"card-fields-verification_value-xli79h1h4xj00000\"]").content_frame.get_by_label("Security code").fill("777\\")
    page.get_by_role("button", name="Pay now").click()
    page.locator("select[name=\"phone_country_select\"]").select_option("IL")
    page.get_by_placeholder("Email or mobile phone number").select_option("IL")
    page.get_by_placeholder("Email or mobile phone number").click()
    page.get_by_placeholder("Email or mobile phone number").fill("+972544608611")
    page.get_by_role("button", name="Pay now").click()
    page.goto("https://drpt-external-dev.myshopify.com/checkouts/cn/Z2NwLWV1cm9wZS13ZXN0MTowMUpCUUFWMThENVcyU1o0Mk5TUThaUUtWRg/thank-you")
    expect(page.get_by_role("heading", name="Your order is confirmed")).to_be_visible()
    expect(page.get_by_role("heading", name="Thank you!")).to_be_visible()
