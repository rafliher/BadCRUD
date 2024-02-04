import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class XSSDetectionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost"

    def test_1_login_correct_credentials(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def test_2_go_to_xss_page(self):
        xss_url = self.url + '/xss.php'
        self.browser.get(xss_url)

        # Enter a value in the text field
        input_field = self.browser.find_element(By.NAME, 'thing')
        input_value = '<script>alert("XSS Attack!");</script>'
        input_field.send_keys(input_value)

        # Submit the form
        submit_button = self.browser.find_element(By.NAME, 'submit')
        submit_button.click()

        # Check if the alert pops up
        alert = self.browser.switch_to.alert
        self.assertEqual('XSS Attack!', alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
