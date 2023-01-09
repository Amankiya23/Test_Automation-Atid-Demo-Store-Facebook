from selenium.webdriver.common.by import By
import time
from Facebook.Test.Base_test.Base import *

from Facebook.BaseTest.login_locators import *

class Test(BaseTest):


    def test1_login(self):
        driver = super().test_init()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, Email)
        coupon.clear()
        coupon.send_keys(Email_send_key1)
        time.sleep(7)
        coupon = driver.find_element(By.NAME, Pass)
        coupon.clear()
        coupon.send_keys(Pass_send_key1)
        time.sleep(5)
        driver.find_element(By.XPATH, Login1).click()
        time.sleep(5)
        super().tear_down()

    def test2_login(self):
        driver = super().test_init()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, Email)
        coupon.clear()
        coupon.send_keys(Email_send_key1)
        time.sleep(7)
        driver.find_element(By.XPATH, Login).click()
        time.sleep(5)
        super().tear_down()


    def test3_login(self):
        driver = super().test_init()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, Email)
        coupon.clear()
        coupon.send_keys(Email_send_key2)
        time.sleep(7)
        coupon = driver.find_element(By.ID, Pass)
        coupon.clear()
        coupon.send_keys(Pass_send_key2)
        time.sleep(5)
        driver.find_element(By.XPATH, Login).click()
        time.sleep(5)
        super().tear_down()


    def test4_login(self):
        driver = super().test_init()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, Email)
        coupon.clear()
        coupon.send_keys()
        time.sleep(1)
        coupon = driver.find_element(By.ID, Pass)
        coupon.clear()
        coupon.send_keys()
        time.sleep(1)
        driver.find_element(By.XPATH, Login).click()
        time.sleep(5)
        super().tear_down()


