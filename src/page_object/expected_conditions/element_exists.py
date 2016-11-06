from selenium.webdriver.remote.webelement import WebElement


class element_exists():
    """
    Expected Condition for waiting for element to exists.
    """

    def __init__(self, element):
        self.element = element

    def __call__(self, drivers=None):
        if isinstance(self.element, WebElement):
            return True

        return self.element.exists()
