import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage

def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    home_page = HomePage(page)
    #expect(home_page.upgrade_button).to_be_visible()
    home_page.is_upgrade_button_visible()
    home_page.click_performance_link()
    home_page.click_dashboard_link()