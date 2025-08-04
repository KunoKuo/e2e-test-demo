from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()

    # Yahoo 首頁的搜尋欄位 name 叫 'q'
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("pytest selenium")
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0
    driver.quit()
