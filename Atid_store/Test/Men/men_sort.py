import time
from Atid_store.Test.Base_test.Base import *
from selenium.webdriver.common.by import By


class Test_filter(BaseTest):

#  sort a product by latest
    def test_menaccessories_sort(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/form[1]/select[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[contains(text(),'Sort by latest')]").click()
        time.sleep(2)
        super().tear_down()

#  sort a product by low to high
    def test_men_sort(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/form[1]/select[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[contains(text(),'Sort by price: low to high')]").click()
        time.sleep(5)
        super().tear_down()

#  sort a product by high to low
    def test_men_sort(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/form[1]/select[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[contains(text(),'Sort by price: high to low')]").click()
        time.sleep(5)
        super().tear_down()

