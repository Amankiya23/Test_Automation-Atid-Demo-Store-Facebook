import time

from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from Atid_store.Test.Base_test.Base import *
from Atid_store.Test.Base_test.Locatores import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Test_search(BaseTest):

# Search a non existing product
    def test_men_search(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='wc-block-search__input-1']")))
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']").send_keys("Black Hoodie", keys.Keys.ENTER)
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, "//h1[contains(text(),'Black Hoodie')]").text
        assert product_name == "Black Hoodie"
        super().tear_down()
    def test_men_search_normal(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("Black Hoodie")
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        super().tear_down()

# Search a non existing product
    def test_men_search2(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("one love")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        super().tear_down()



# Search a null product
    def test_men_search3(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//input[@id='wc-block-search__input-1']")
        search.clear()
        search.send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/*[1]").click()
        time.sleep(5)
        super().tear_down()