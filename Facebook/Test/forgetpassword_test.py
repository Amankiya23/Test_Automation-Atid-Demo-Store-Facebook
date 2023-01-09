from selenium.webdriver.common.by import By
import time
from Facebook.Test.Base_test.Base import *
from Facebook.BaseTest.forgetpassword_locators import *

class Test(BaseTest):

    def test_forgetpassword1(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Forgetpassword).click()
        time.sleep(2)
        coupon = driver.find_element(By.ID, Forgetpassword_tab)
        coupon.clear()
        coupon.send_keys(Incorrect_email__send_key)
        time.sleep(7)
        driver.find_element(By.XPATH, Button).click()
        time.sleep(2)
        super().tear_down()

    def test_forgetpassword2(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Forgetpassword).click()
        time.sleep(2)
        coupon = driver.find_element(By.ID, Forgetpassword_tab)
        coupon.clear()
        coupon.send_keys()
        time.sleep(7)
        driver.find_element(By.XPATH, Button).click()
        time.sleep(2)
        super().tear_down()

    def test_forgetpassword3(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Forgetpassword).click()
        time.sleep(2)
        coupon = driver.find_element(By.ID, Forgetpassword_tab)
        coupon.clear()
        coupon.send_keys(Email_send_key)
        time.sleep(7)
        driver.find_element(By.XPATH, Button).click()
        time.sleep(2)
        super().tear_down()