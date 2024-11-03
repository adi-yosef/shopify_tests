import datetime
from playwright.sync_api import sync_playwright, Page
import pytest
from src.config.config import TestData
from src.pom.cart_page import CartPage
from src.pom.dropit_chips_page import DropItChipsPage
from src.pom.dropit_hamburger_page import DropItBurgerPage
from src.pom.home_page import HomePage
from src.pom.login_page import LoginPage
from src.pom.up_menu_page import UpMenuPage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="function")
def set_up_tear_down():
    start_time = datetime.datetime.now()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=200)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        print("Run Started at : " + str(start_time))
        print("Chrome Environment Set Up")
        print("--------------------------------------------------------")
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
        login_page = LoginPage(page)
        login_page.run_login(TestData.ADMIN_PASS)
        page.wait_for_load_state("networkidle")
        print("Login Pass")
        yield page
        context.close()
        browser.close()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f"Test duration: {elapsed_time.total_seconds():.2f} seconds")

@pytest.fixture
def page(set_up_tear_down) -> Page:
    return set_up_tear_down

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def up_menu_page(page: Page) -> UpMenuPage:
    return UpMenuPage(page)

@pytest.fixture
def dropit_hamburger_page(page: Page) -> DropItBurgerPage:
    return DropItBurgerPage(page)

@pytest.fixture
def dropit_chips_page(page: Page) -> DropItChipsPage:
    return DropItChipsPage(page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)
