from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os


class MyWebDrive:

    def __init__(self, path_input: str = "input", headless: bool = True):

        self.path_input = os.path.join(os.getcwd(), path_input)
        self.headless = headless
        self.drive = self.create()

    def create(self):

        options = Options()

        if self.headless:
            options.add_argument("-headless")

        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", self.path_input)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        options.add_argument("-no-sandbox")
        options.add_argument("-disable-dev-shm-usage")
        options.add_argument("-disable-blink-features=AutomationControlled")
        options.add_argument("-disable-extensions")
        options.add_argument("-incognito")
        drive = webdriver.Chrome(options=options)

        return drive
