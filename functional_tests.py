from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
    
        self.browser.get('http://localhost:8002')
        self.assertIn('Donation', self.browser.title)
        # the user see list of donation cases
        # the user click on a donation case and get the details
        # the user can donate to the case by submitting his info
        # in the user account hwe have the cases that hw submitted to track it

if __name__ == '__main__':
 unittest.main(warnings='ignore')