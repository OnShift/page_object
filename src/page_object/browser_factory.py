import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


class BrowserFactory(object):

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")

    def selenium_browser(self):
        browser = str(os.getenv('BROWSER', None))
        if browser == "HEADLESS":
            display = Display(visible=0, size=(800, 600))
            display.start()
        return webdriver.Chrome(chrome_options=self.chrome_options)
