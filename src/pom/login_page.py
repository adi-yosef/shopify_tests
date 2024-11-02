import src.config.config

class LoginPage:
    def __init__(self, page) -> None:
        self.page = page

        self.admin_password = src.config.config.TestData.ADMIN_PASS
        self.password_box = page.get_by_label("Enter store password")
        self.enter_button = page.get_by_role("button", name="Enter")


    def enter_password(self, password: str):
        self.password_box.clear()
        self.password_box.fill(password)

    def click_enter(self):
        self.enter_button.click()

    def run_login(self, password: str):
        self.enter_password(password)
        self.click_enter()
