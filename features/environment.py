#This will be the setup and teardown
from playwright.sync_api import sync_playwright
import time

def before_feature(context, feature):
    #setup
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False,
        slow_mo=1000,
        channel='chrome'
    )
    context.page = context.browser.new_page()

def after_feature(context, feature):
    # Teardown
    context.page.close()
    context.browser.close()
    context.playwright.stop()
    time.sleep(2)

