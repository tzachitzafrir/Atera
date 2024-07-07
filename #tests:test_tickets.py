#tests/test_tickets.py

from playwright.sync_api import sync_playwright
from webpages import dashboard_page, tickets_page  # Import modules from webpages 
from webpages.login_page import  DEVICES_URL # Import constants
from webpages.dashbaord_page import  DASHBOARD_URL
import re


def pull_num_open_tickets():
    """
    Asserting URL, titles and pulling number of open tickets
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch Chromium browser
        context = browser.new_context()  # Create a new browser context
        page = context.new_page()  # Create a new page within the context
        
        try:
            page.goto(DASHBOARD_URL)            

            # Assert the tickets tab selector is visible
            assert tickets_page.TICKETS_TAB_SELECTOR.is_visible(), "Tickets tab selector is not visible"

            # Assert table is showing open tickets
            assert tickets_page.STATUS_COLUMN_OPEN_STATUS_SELECTOR .is_visible(), "Open ticket status selector is not visible"

            # Get the inner text of the element (which contains the number of open tickets)
            num_tickets_dispaly_text = tickets_page.NUM_TICKETS_DISPALY_SELECTOR.inner_text()

            # Print the extracted text 
            print(f"Text display: {num_tickets_display_text}")

			# Using regex to extract only digits from the text
            # This regex pattern removes all non-digit characters
            tickets_numeric = re.sub(r'\D', '', num_tickets_dispaly_text)

            # Convert the extracted numeric string to an integer
            open_tickets_count = int(tickets_numeric)

            return open_tickets_count
            
               
        except AssertionError as e:
            print(f"Error: {e}")
            return None

## Additioanl tests that can be verified: check filter options and table updated accordingly, check different viewes, chck actions os a ticket 
## check flow for a new ticket (all options), check lifecycle of a new ticket (from open to pending, to resolved), check drill down to a specific ticket etc..

### 2nd option, less modular- implementing navigation to tickets page ###  
#    def navigating_tickets():
#    with sync_playwright() as p:
#       browser = p.chromium.launch(headless=False)  # Launch Chromium browser
#       context = browser.new_context()  # Create a new browser context
#       page = context.new_page()  # Create a new page within the context
#        
#       try:
#           page.goto(DASHBOARD_URL)   
#           dashbaord_page.SIDEBAR_TICKETS_SELECTOR.click()              
#
#           # Wait for navigation to complete
#           page.wait_for_navigation()
#
#           # Asserting tickets url is correct
#           assert page.url == TICKETS_URL, f"Expected URL: {TICKETS_URL}, Actual URL: {page.url}"
#            
#           # Asserting header of tickes webpage
#           assert tickets_page.TICKETS_HEADER_SELECTOR.is_visible(), "Tickets header selector is not visible"
#
#           print("Navigation successful!")
#            
#        
#       except AssertionError as e:
#           print(f"Assertion Error: {e}")
