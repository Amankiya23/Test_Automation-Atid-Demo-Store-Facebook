from selenium import webdriver



class BaseTest():
    driver = webdriver.Chrome()

    def test_init(self):
        self.driver.get("https://www.facebook.com//")
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        if self.driver==True:
            self.driver.quit()
            self.driver.close()

