import datetime
from playwright.sync_api import Playwright, Page
import pytest
import src.config.config
from src.pom.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def set_up_tear_down(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=200)
    context = browser.new_context(no_viewport=True)
    print("Run Started at : " + str(datetime.datetime.now()))
    print("Chrome Environment Set Up")
    print("--------------------------------------------------------")
    page = context.new_page()
    navigate(page, src.config.config.TestData.BASE_URL)
    page.wait_for_load_state("networkidle")
    login_page = LoginPage(page)
    login_page.run_login(login_page.admin_password)
    print("yeah login pass")
    yield page
    context.close()
    browser.close()


def navigate(page, url):
    page.goto(url)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)