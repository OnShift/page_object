import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserFactory(object):

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    drivers = {
        "CHROME": "_chrome_driver",
        "HEADLESS": "_headless_driver",
        "FIREFOX": "_firefox_driver",
        "SAFARI": "_safari_driver",
        "REMOTE": "_remote_driver"
    }

    def selenium_browser(self):
        browser = str(os.getenv("BROWSER", "CHROME"))
        return getattr(self, self.drivers[browser])()

    def _headless_driver(self):
        self.chrome_options.add_argument("--headless")
        return self._chrome_driver()

    def _chrome_driver(self):
        return webdriver.Chrome(chrome_options=self.chrome_options)

    def _firefox_driver(self):
        return webdriver.Firefox()

    def _safari_driver(self):
        return webdriver.Safari()

    def _remote_driver(self):
        url = str(os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub"))
        capability = str(os.getenv("CAPABILITY", "EDGE"))
        return webdriver.Remote(url, getattr(webdriver.DesiredCapabilities, capability))
