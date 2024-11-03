from playwright.sync_api import Page, expect
from ..pom.home_page import HomePage

def search_item_and_click_on_it(
    item_name: str,
    description: str,
    page: Page
) -> None:
    home_page = HomePage(page)
    home_page.click_on_search_button()
    home_page.page.fill("input[placeholder='Search']", item_name)
    print(f"Search for {item_name}")
    home_page.page.get_by_role("link", name=description).click()
    print(f"Clicking on {item_name}")
    expect(home_page.page.get_by_role("heading", name=description)).to_be_visible()
    print("We are on the right item page")
