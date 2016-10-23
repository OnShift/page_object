from page_object.browser_factory import BrowserFactory


class Browser():
    _factory = None
    _browser = None

    @classmethod
    def selenium_browser(cls):
        if cls._browser is None:
            cls._browser = cls.factory().selenium_browser()
        return cls._browser

    @classmethod
    def factory(cls):
        if cls._factory is None:
            cls._factory = BrowserFactory()
        return cls._factory
