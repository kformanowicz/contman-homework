from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome()

    def close(self):
        Browser.driver.close()
