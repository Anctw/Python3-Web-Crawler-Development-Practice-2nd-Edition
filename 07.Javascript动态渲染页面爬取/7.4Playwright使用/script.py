import re
from playwright.sync_api import Playwright, sync_playwright, expect
"""4.代码生成"""
"""这段代码由操作生成代码"""

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("code")
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("button", name="百度一下").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
