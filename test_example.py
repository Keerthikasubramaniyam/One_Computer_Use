# from playwright.sync_api import sync_playwright
# import random

# def generate_random_email():
#     return f"testuser{random.randint(100, 999)}@example.com"

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
    
#     # Navigate to the registration page
#     page.goto("https://demoqa.com/automation-practice-form")
    
#     # Fill basic information
#     page.fill('//input[@placeholder="First Name"]', "John")
#     page.fill('//input[@placeholder="Last Name"]', "Doe")
#     page.fill('//input[@id="userEmail"]', generate_random_email())
#     page.check('input[value="Male"]')
#     page.fill('//input[@id="userNumber"]', "1234567890")
    
#     # Select gender (Male)
   
    
#     # # Submit the form
#     page.click('//button[@id="submit"]')
    
#     # # Take screenshot
#     page.screenshot(path="registration_success.png")
#     page.click('//button[@id="closeLargeModal"]')
    
#     browser.close()


from playwright.sync_api import sync_playwright
import random

def generate_random_email():
    return f"testuser{random.randint(100, 999)}@example.com"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)  # slow_mo for demo/debug
    page = browser.new_page()
    
    # Navigate to the registration page
    page.goto("https://demoqa.com/automation-practice-form")

    # Fill in the form
    page.fill('#firstName', "John")
    page.fill('#lastName', "Doe")
    page.fill('#userEmail', generate_random_email())
    page.check('input[name="gender"][value="Male"]')
    page.fill('#userNumber', "1234567890")

    # Set date of birth (optional)
    # page.click('#dateOfBirthInput')
    # page.select_option('.react-datepicker__month-select', value='5')  # June
    # page.select_option('.react-datepicker__year-select', value='1990')
    # page.click('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)')

    # Submit the form
    page.click('#submit')

    # Wait for modal and take screenshot
    page.wait_for_selector('#example-modal-sizes-title-lg', timeout=5000)
    page.screenshot(path="registration_success.png")

    # Close the modal
    page.click('#closeLargeModal')

    browser.close()

