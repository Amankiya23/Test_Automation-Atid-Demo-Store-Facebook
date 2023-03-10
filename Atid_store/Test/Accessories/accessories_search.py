import time
from Atid_store.Test.Base_test.Base import *
from selenium.webdriver.common.by import By


class Test_search(BaseTest):

# Search a non existing product
    def test_women_search(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("Blue Denim Shorts")
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, "//h1[contains(text(),'Blue Denim Shorts')]").text
        assert product_name == "Blue Denim Shorts"
        super().tear_down()


# Search a non existing product
    def test_women_search2(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("kiss")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        super().tear_down()



# Search a null product
    def test_women_search3(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        super().tear_down()