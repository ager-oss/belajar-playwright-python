import re
from playwright.sync_api import Page, expect
import pytest
import csv

from conftest import page

def get_csv_data():
    data = []
    with open("./test_data/data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)  # Assuming username is in column 0 and password in column 1
    return data


@pytest.mark.parametrize("username,password", get_csv_data())

def test_example(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()

  