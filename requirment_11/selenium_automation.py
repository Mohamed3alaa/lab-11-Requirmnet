from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os


options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get('https://www.amazon.eg/-/en/')
    driver.maximize_window()
    time.sleep(2)

    search_term = "PS4"
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(search_term, Keys.RETURN)
    time.sleep(2)

    first_product = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] a")
    first_product.click()
    time.sleep(2)

    product_title = driver.find_element(By.ID, 'productTitle').text
    product_url = driver.current_url

    try:
        product_price = driver.find_element(By.ID, 'corePriceDisplay_desktop_feature_div').text
    except:
        product_price = "Price not available"

    try:
        product_rating = driver.find_element(By.CSS_SELECTOR, '#acrPopover > span.a-declarative > a > span').text
    except:
        product_rating = "Rating not available"

    
    print(f"Product URL: {product_url}")
    print(f"Product Title: {product_title}")
    print(f"Product Price: {product_price}")
    print(f"Product Rating: {product_rating}")

    screenshot_path = os.path.join(os.getcwd(), 'PS4_screenshot.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    driver.quit()