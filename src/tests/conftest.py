import datetime
from playwright.sync_api import sync_playwright, Page
import pytest
import src.config.config
from src.pom.cart_page import CartPage
from src.pom.drop_it_chips_page import DropItChipsPage
from src.pom.dropit_hamburger_page import DropItBurgerPage
from src.pom.home_page import HomePage
from src.pom.login_page import LoginPage
from src.pom.up_menu_page import UpMenuPage


@pytest.fixture(scope="function", autouse=True)
def set_up_tear_down(playwright):
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
