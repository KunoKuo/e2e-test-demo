from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_yahoo_search(driver):
    driver.get("https://www.yahoo.com")

    # 使用 WebDriverWait 等待搜尋欄位出現，最多等 10 秒
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "p")))

    # Yahoo 首頁的搜尋欄位 name 叫 'p'
    search_input.send_keys("pytest selenium")
    search_input.send_keys(Keys.RETURN)

    # 等待至少一個搜尋結果標題 (h3) 出現
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

    # Yahoo 的搜尋結果標題可能是 <h3> 或 <h3 class="title"> 裡的 a
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0
