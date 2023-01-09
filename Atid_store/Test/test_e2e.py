import time
from Atid_store.Test.Base_test.Base import *
from Atid_store.Test.Base_test.Locatores import *

from selenium.webdriver.common.by import By


# This Test add a product from store to the chart with coupon
class Test_e2e(BaseTest):


    def test_store(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[8]/div[1]/a[1]/img[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, "coupon_code")
        coupon.clear()
        coupon.send_keys("0000")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Apply coupon')]").click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, "//a[contains(text(),'Basic Gray Jeans')]").text
        assert product_name == "Basic Gray Jeans"
        super().tear_down()

    # This Test add a product from Men to the chart with coupon
    def test_men(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Men).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Product_men).click()
        time.sleep(2)
        driver.find_element(By.XPATH, men_cart).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Cart_cheak_men).click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, men_coupon)
        coupon.clear()
        coupon.send_keys(Coupon_send_keys_men)
        time.sleep(2)
        driver.find_element(By.XPATH, Coupone_button_men).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, Productname_men).text
        assert product_name == "Black Hoodie"
        super().tear_down()

    # This Test add a product from women to the chart with coupon
    def test_women(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH,Women).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Product_Women).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Women_cart).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Cart_cheak_Women).click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, Women_coupon)
        coupon.clear()
        coupon.send_keys(Coupon_send_keys_Women)
        time.sleep(2)
        driver.find_element(By.XPATH, Coupone_button_Women).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, Productname_Women).text
        assert product_name == "Bright Red Bag"
        super().tear_down()

    # This test select a product from accessosories to END Process With login
    def test_accessosories(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Accessosories).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Product_accessosories).click()
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories_cart).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Cart_cheak_accessosories).click()
        coupon = driver.find_element(By.NAME, accessosories_coupon)
        coupon.clear()
        coupon.send_keys(Coupon_send_keys_accessosories)
        time.sleep(2)
        driver.find_element(By.XPATH, Coupone_button_accessosories).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, Productname_accessosories).text
        assert product_name == "Buddha Bracelet"
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories_procced).click()
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories_login).click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories_username)
        coupon.clear()
        coupon.send_keys(enter_first_name1)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories_password)
        coupon.clear()
        coupon.send_keys(enter_last_name1)
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories_login2).click()
        super().tear_down()

    # This test select a product from accessosories to END TO END Process
    def test_accessosories2(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, Accessosories2).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Product_accessosories2).click()
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories2_cart).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Cart_cheak_accessosories2).click()
        coupon = driver.find_element(By.NAME, accessosories2_coupon)
        coupon.clear()
        coupon.send_keys(Coupon_send_keys_accessosories2)
        time.sleep(2)
        driver.find_element(By.XPATH, Coupone_button_accessosories2).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, Productname_accessosories2).text
        assert product_name == "Boho Bangle Bracelet"
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories2_procced).click()
        coupon = driver.find_element(By.NAME, accessosories2_first_name)
        coupon.clear()
        coupon.send_keys(enter_first_name)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_last_name)
        coupon.clear()
        coupon.send_keys(enter_last_name)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_Company_name)
        coupon.clear()
        coupon.send_keys(enter_Company_name)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_first_name)
        coupon.clear()
        coupon.send_keys(enter_first_name)
        time.sleep(2)
        driver.find_element(By.XPATH, accessosories2_Country_Region).click()
        time.sleep(2)
        driver.find_element(By.XPATH, enter_Country_Region).click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_Street_address)
        coupon.clear()
        coupon.send_keys(enter_Street_address)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_Street_unit)
        coupon.clear()
        coupon.send_keys(enter_Street_unit)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_Postcode_ZIP)
        coupon.clear()
        coupon.send_keys(enter_Postcode_ZIP)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_city)
        coupon.clear()
        coupon.send_keys(enter_city)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_phone)
        coupon.clear()
        coupon.send_keys(enter_Phone)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, accessosories2_Email_address)
        coupon.clear()
        coupon.send_keys(enter_Email_address)
        time.sleep(2)
        driver.find_element(By.XPATH, place_order).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH, Placeorder_accessosories2).text
        assert product_name == "Checkout"
        super().tear_down()

    # This test add sale products with a price of 72 and above to chart
    def test_limitation(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, men_sale).click()
        nav = driver.find_element(By.XPATH, Nav_ul)
        na = nav.find_elements(By.TAG_NAME, Na_il)
        gap = driver.find_element(By.XPATH, wom_ul)
        ga = gap.find_elements(By.TAG_NAME, wo_il)
        for n in na:

            if n.text == 'ATID Blue Shoes':
                n.click()
                break
        driver.find_element(By.XPATH, Blue_shoes_men).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Blue_shoes_men_chart).click()
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, product_limitation_men1).text
        assert product_name == "ATID Blue Shoes"
        time.sleep(2)
        driver.find_element(By.XPATH, men_sale).click()
        for n in na:

            if n.text == 'ATID Yellow Shoes':
                n.click()
                break

        driver.find_element(By.XPATH, yellow_shoes).click()
        time.sleep(2)
        driver.find_element(By.XPATH, yellow_shoes_chart).click()
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, product_limitation_men2).text
        assert product_name == "ATID Yellow Shoes"
        time.sleep(2)
        driver.find_element(By.XPATH, women_sale).click()
        for m in ga:
            if m.text == 'Blue Denim Shorts':
                m.click()
                break
        driver.find_element(By.XPATH, Blue_Denium_shorts).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Blue_Denium_shorts_chart).click()
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, product_limitation_women1).text
        assert product_name == "Blue Denim Shorts"
        time.sleep(2)
        driver.find_element(By.XPATH, women_sale).click()
        for m in ga:
            if m.text == 'Bright Gold Purse With Chain':
                m.click()
                break
        driver.find_element(By.XPATH, Bright_gold_purse).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Bright_gold_purse_chart).click()
        time.sleep(10)
        product_name = driver.find_element(By.XPATH, product_limitation_women2).text
        assert product_name == "80.00 ₪"
        time.sleep(2)
        driver.find_element(By.XPATH, sale_cart).click()
        super().tear_down()

    # This test add only the product with 5 star rank
    def test_star(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, star_store).click()
        time.sleep(2)
        product = driver.find_element(By.XPATH, product_star)
        star = product.find_elements(By.TAG_NAME, boho_five_star)
        for a in star:
            if a.text == 'Boho Bangle Bracelet':
                a.click()
                break
        driver.find_element(By.XPATH, boho_five_star_pro).click()
        time.sleep(2)
        driver.find_element(By.XPATH, boho_five_star_chart).click()
        time.sleep(2)
        product_name = driver.find_element(By.XPATH, product_five_star).text
        assert product_name == "Rated out of 5 based on\n1\ncustomer rating"
        super().tear_down()

    # This test Sends a Question for the site admin

    def test_question(self):
        driver = super().test_init()
        time.sleep(2)
        driver.find_element(By.XPATH, contact_us).click()
        time.sleep(2)
        coupon = driver.find_element(By.NAME, question_name)
        coupon.clear()
        coupon.send_keys(question_name_send_key)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, subject_name)
        coupon.clear()
        coupon.send_keys(subject_name_send_key)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, question_email)
        coupon.clear()
        coupon.send_keys(question_email_send_key)
        time.sleep(2)
        coupon = driver.find_element(By.NAME, question_message)
        coupon.clear()
        coupon.send_keys(question_message_send_key)
        time.sleep(2)
        driver.find_element(By.XPATH, question_submit).click()
        time.sleep(5)
        product_name = driver.find_element(By.XPATH,
                                           "//h3[contains(text(),'Have any Queries? We're here to help.')]").text
        assert product_name == "Have any Queries? We're here to help."
        super().tear_down()
