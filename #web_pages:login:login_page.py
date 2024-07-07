#web_pages/login/login_page.py

from playwright.sync_api import Locator, By

class LoginPage(Page):
    LOGIN_URL = "https://auth.atera.com/u/login"
    DEVICES_URL = "https://app.atera.com/new/devices"

    WELCOME_SELECTOR = Locator(By.CSS_SELECTOR, '.cfa8d68ea')
    LOGIN_SELECTOR = Locator(By.CSS_SELECTOR, '.cc2583be9')
    EMAIL_ADDRESS_SELECTOR = Locator(By.CSS_SELECTOR, '.cdf1d8930')
    PASSWORD_SELECTOR = Locator(By.CSS_SELECTOR, '.cdf1d8930').    
    CONTINUE_BTN_SELECTOR = Locator(By.CSS_SELECTOR, '._button-login-id')



 class LoginPageData:
    WELCOME_TITLE = "Welcome"
    LOGIN_TITLE = "Log in to Atera"

    USERNAME="atera-automation-exercise@atera.com"
    PASSWORD="sjAh8lfE@m~dotC5"   

## USERNAME and PASSWORD can be moved to a seperated credentials.py that gather all needed credentials    
    



 


