import time
from Atid_store.Test.Base_test.Base import *
from selenium.webdriver.common.by import By


class Test_filter(BaseTest):

# Search a filtered product
    def test_accessories_filter(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Filter')]").click()
        time.sleep(10)
        super().tear_down()
