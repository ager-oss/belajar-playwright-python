from playwright.sync_api import sync_playwright, expect
import re

def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No cookie banner found")

    search_box = page.locator('textarea[name="q"]')
    search_box.wait_for(state="visible", timeout=10000)
    search_box.fill("Playwright Python")
    search_box.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
          
    
    
    
    
        