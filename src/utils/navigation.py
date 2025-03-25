class Navigation:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)