from playwright.sync_api import Page, expect

from ..pom.home_page import HomePage
from ..pom.up_menu_page import UpMenuPage
from ..tests.conftest import home_page


def search_item_and_click_on_it(
    item_name: str,
    description: str,
    page: Page

) -> None:
    home_page = HomePage(page)
    home_page.click_on_search_button()
    home_page.fill_search_box(item_name)
    page.get_by_role("link", name=description).click()
    expect(page.get_by_role("heading", name=description)).to_be_visible()
