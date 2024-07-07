#web_pages/dashboard/tickets_page.py

from playwright.sync_api import Locator, By

class TicketsPage(Page):
    TICKETS_HEADER_SELECTOR = Locator(By.CSS_SELECTOR, '.list-page-title')
    TICKETS_TAB_SELECTOR = Locator(By.CSS_SELECTOR, '.mat-tab-label-content')
    NUM_TICKETS_DISPALY_SELECTOR = Locator(By.CSS_SELECTOR, '.list-actions-wrapper .action-buttons p')
    STATUS_COLUMN_OPEN_STATUS_SELECTOR = Locator(By.CSS_SELECTOR, '.cdk-column-status ng-select')
  
