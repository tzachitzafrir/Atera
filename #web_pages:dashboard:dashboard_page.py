#web_pages/dashboard/dashboard_page.py

from playwright.sync_api import Locator, By

class DashboardPage(Page):
    DASHBOARD_URL = "https://app.atera.com/new/dashboard"
    TICKETS_URL = "https://app.atera.com/new/tickets"

    SIDEBAR_DASHBOARD_SELECTOR = Locator(By.CSS_SELECTOR, '.menu-title'[0])
    SIDEBAR_TICKETS_SELECTOR = Locator(By.CSS_SELECTOR, '.menu-title'[1])
    DASHBOARD_HEADER_SELECTOR = Locator(By.CSS_SELECTOR, '.title')[0]
    TICKETS_STATUS_SELECTOR = Locator(By.CSS_SELECTOR, '.items-center'[9])
    ALERT_STATUS_SELECTOR = Locator(By.CSS_SELECTOR, '.items-center'[14])


