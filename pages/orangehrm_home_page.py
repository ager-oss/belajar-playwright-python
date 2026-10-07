from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        #self.logout_link = page.get_by_role("link", name="Logout")
        
    def is_upgrade_button_visible(self):
        return self.upgrade_button.is_visible()
    
    def click_performance_link(self):
        self.performance_link.click()
    
    def click_dashboard_link(self):
        self.dashboard_link.click()
        
    