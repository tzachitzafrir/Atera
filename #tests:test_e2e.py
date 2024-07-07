#tests/test_e2e.py

from playwright.sync_api import sync_playwright
from webpages import login_page, dashboard_page, tickets_page  # Import page modules
from login_page import USERNAME, PASSWORD 
from webpages.login_page import DEVICES_URL  # Import constants
from webpages.dashboard_page import DASHBOARD_URL, TICKETS_URL  # Import constants


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page.login_to_atera(page, USERNAME, PASSWORD)

        # Navigate to dashboard page
        navigate_to(
                page,
                DEVICES_URL,
                click_selector=dashboard_page.SIDEBAR_DASHBOARD_SELECTOR,
                wait_for_selector=dashboard_page.DASHBOARD_HEADER_SELECTOR,
                assert_url=DASHBOARD_URL,
                assert_visible=dashboard_page.ALERT_STATUS_SELECTOR
            )
 		
 		# Navigate to tickets page
        navigate_to(
                page,
                DASHBOARD_URL,
                click_selector=dashboard_page.SIDEBAR_TICKETS_SELECTOR,
                wait_for_selector=tickets_page.TICKETS_HEADER_SELECTOR,
                assert_url=TICKETS_URL,
                assert_visible=tickets_page.TICKETS_TAB_SELECTOR
            )
        
        tickets_page.pull_num_open_tickets(page)


        browser.close()