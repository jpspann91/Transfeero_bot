from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
import time, logging
# Set up the browser (Chromium in this case)
driver = webdriver.Chrome()  # Make sure you have the appropriate WebDriver installed and in PATH

try:
    # Open the website
    driver.get('https://automationintesting.com/selenium/testpage/')

    # Find all buttons with the same class name

    first_name_field = driver.find_element(By.ID, 'firstname')
    first_name_field.click()
    first_name_field.send_keys('FILLING')
    
    first_name_value = first_name_field.get_attribute('value')
    
    sur_name_field = driver.find_element(By.ID, 'surname')
    sur_name_field.click()
    sur_name_field.send_keys('WITH INFORMATION')
    
    sur_name_value = sur_name_field.get_attribute('value')

    file = open('new_file.txt', 'w')
    
    file.write(f"{first_name_value}, {sur_name_value}")
    
    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=6, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda d : first_name_field.send_keys(" THIS OUT") or True)
    
    buttons = driver.find_elements(By.CLASS_NAME, 'btn-primary')
    # Click each button
    print(buttons)
    time.sleep(5)
    for button in buttons:
        button.click()
except Exception as e:
    logging.exception(e)
finally:
    time.sleep(5)
    print('THIS SHOULD END')
    # Close the browser
    driver.quit()
