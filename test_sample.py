
from playwright.sync_api import sync_playwright, expect

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to Google
        page.goto("https://www.google.com")

        # Verify the page title
        expect(page).to_have_title("Google")

        print("Test Passed: Google title verified!")

        browser.close()