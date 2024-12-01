from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_user_can_get_list_of_cases(self):
    
        self.browser.get('http://localhost:8002')
        self.assertIn('Donation', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        # the user see list of donation cases
        self.assertIn('Cases', header_text)

        # the user click on a donation case and get the details
        # the user can donate to the case by submitting his info
        # in the user account hwe have the cases that are submitted to track it

if __name__ == '__main__':
 unittest.main(warnings='ignore')