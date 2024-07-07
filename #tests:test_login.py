#tests/test_login.py

from playwright.sync_api import sync_playwright
from webpages import login_page  # Import login_page module from webpages
from webpages.login_page import LOGIN_URL, DEVICES_URL, USERNAME, PASSWORD  # Import constants

def login_to_atera(username, password):
	 """
    Login to app given username and password, and asserting titles and url
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch Chromium browser
        context = browser.new_context()  # Create a new browser context
        page = context.new_page()  # Create a new page within the context
        
        try:
            # Navigate to the login page and check titles visible
            page.goto(LOGIN_URL)
            assert login_page.WELCOME_SELECTOR.is_visible(), "Welcome selector is not visible"
			assert login_page.LOGIN_SELECTOR.is_visible(), "Login selector is not visible"

			# Asserting welcome title is correct
            welcome_text = page.inner_text(login_page.WELCOME_SELECTOR)
            expected_welcome_text = login_page.WELCOME_TITLE
            assert welcome_text == expected_welcome_text, f"Welcome title isn't correct. Expected '{expected_welcome_text}', but got '{welcome_text}'"
            
            # Asserting login title is correct
            login_text = page.inner_text(login_page.LOGIN_SELECTOR)
            expected_login_text = login_page.LOGIN_TITLE
            assert login_text == expected_login_text, f"Login title isn't correct. Expected '{expected_login_text}', but got '{login_text}'"
            
            # Fill in the username field, click continue and fill in password field
            assert login_page.EMAIL_ADDRESS_SELECTOR.is_visible(), "Email address field is not visible"
            login_page.EMAIL_ADDRESS_FIELD.fill(USERNAME)
            assert login_page.CONTINUE_BTN_SELECTOR.is_visible(), "Continue button is not visible"
            login_page.CONTINUE_BTN.click()
            assert login_page.PASSWORD_SELECTOR.is_visible(), "Password field is not visible"
            login_page.PASSWORD_FIELD.fill(PASSWORD)

            # Submit the form and wait for navigation
            page.wait_for_navigation()
            
            # Assert user is directed to devices page in dashboard
            assert page.url == DEVICES_URL, f"Expected URL: {DEVICES_URL}, Actual URL: {page.url}"
            
            print("Login successful!")
        
        except AssertionError as e:
            print(f"Login failed: {e}")



## Additioanl tests that can be verified: check forgot password flow, check corner cases for username and passwords inputs,  
## check edit the username etc..                 
       

