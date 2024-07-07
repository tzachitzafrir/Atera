from playwright.sync_api import sync_playwright
from webpages import dashboard_page  # Import dashbaord_page module from webpages
from webpages.login_page import  DEVICES_URL # Import constants



def navigate_to(page, url, click_selector=None, wait_for_selector=None, assert_url=None, assert_visible=None):
    """
    Navigate to a URL, click an element, wait for an element, and assert URL and visibility.
    """
    with page.expect_navigation():
        page.goto(url)

    if click_selector:
        page.click(click_selector)

    if wait_for_selector:
        page.wait_for_selector(wait_for_selector)

    if assert_url:
        assert page.url == assert_url, f"Expected URL: {assert_url}, Actual URL: {page.url}"

    if assert_visible:
        assert assert_visible.is_visible(), f"{assert_visible.selector} is not visible"

    print("Navigation to {url} successful!")   


## Option to move the 'navigating_to' func to a common page with other additioanl common funcs

## Additioanl tests that can be verified: check each widget has data, check in tickets status that there are less then 10 (for example) overdue tickets, 
## check in alert status that there are less then 5 (for example) critical alerts, check that edit widgets location/hide widget is possible etc..  


### 2nd option, less modular- implementing navigation to dashboard page ###  
#    def navigating_dashbaord():
#    with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False)  # Launch Chromium browser
#        context = browser.new_context()  # Create a new browser context
#        page = context.new_page()  # Create a new page within the context
#        
#        try:
#            page.goto(DEVICES_URL)   # User is directed to devices page after login
#			dashbaord_page.SIDEBAR_DASHBOARD_SELECTOR.click()	           
#
#			# Wait for navigation to complete
#           page.wait_for_navigation()
#
#			# Asserting dashabord url is correct
#           assert page.url == DASHBOARD_URL, f"Expected URL: {DASHBOARD_URL}, Actual URL: {page.url}"
#            
#            # Asserting widgets titles are visible
#            assert dashboard_page.TICKETS_STATUS_SELECTOR.is_visible(), "Tickets status selector is not visible"
#			assert dashbaord_page.ALERT_STATUS_SELECTOR.is_visible(), "Alert status selector is not visible"
#
#            print("Navigation successful!")
#                    
#        except AssertionError as e:
#            print(f"Navigation Failed: {e}")
