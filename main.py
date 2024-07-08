from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
import time, logging, os
from dotenv import load_dotenv

# Set up the browser (Chromium in this case)
driver = webdriver.Chrome()  # Make sure you have the appropriate WebDriver installed and in PATH
load_dotenv()


try:
    # Open the website
    driver.get('https://account.transfeero.com/')
    
    time.sleep(5)
    
    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    
    print(f"{user_name}, {password}")
    
    user_name_field = driver.find_element(By.ID, 'email')
    user_name_field.click()
    user_name_field.send_keys(user_name)
    
    password_field = driver.find_element(By.ID, 'Password')
    password_field.click()
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.ID, 'login_button_main')
    login_button.click()
     
except Exception as e:
    logging.exception(e)
    
finally:
    time.sleep(15)
    print('THIS SHOULD END')
    # Close the browser
    driver.quit()