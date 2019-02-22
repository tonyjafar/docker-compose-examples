#!/Users/tony/Desktop/Scripts/venv/bin/python -W ignore
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# caps = DesiredCapabilities.CHROME
# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument("privileged")
# options.add_argument("no-sandbox")
# options.add_argument("disable-gpu")
# options.add_argument("window-size=1200x800")


caps = DesiredCapabilities.FIREFOX
caps['marionette'] = True
options = webdriver.FirefoxOptions()
options.headless = True


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       options=options,
                                       desired_capabilities=caps)

    def get_github(self):
        driver = self.driver
        driver.get("https://github.com")
        title = driver.title
        self.assertEqual(title, 'The world’s leading software development platform · GitHub', "title is not correct")

    def test_get_github(self):
        self.get_github()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
