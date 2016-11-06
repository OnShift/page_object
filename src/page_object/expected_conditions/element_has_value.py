from selenium.common.exceptions import StaleElementReferenceException


class element_has_value():
    """
    Expected Condition for waiting for element to have a specific value.
    """

    def __init__(self, accessor, comparator):
        self.accessor = accessor
        self.comparator = comparator

    def __call__(self, driver):
        try:
            current_value = self.accessor()
            return self.comparator(current_value)
        except StaleElementReferenceException:
            return False
