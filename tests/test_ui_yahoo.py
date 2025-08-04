from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_yahoo_search():
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.com")

    # 等頁面加載，點擊搜尋欄之前要確認它出現
    time.sleep(2)

    # Yahoo 首頁的搜尋欄位 name 叫 'p'
    search = driver.find_element(By.NAME, "p")
    search.send_keys("pytest selenium")
    search.send_keys(Keys.RETURN)

    # 等待搜尋結果載入
    time.sleep(2)

    # Yahoo 的搜尋結果標題可能是 <h3> 或 <h3 class="title"> 裡的 a
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0

    driver.quit()