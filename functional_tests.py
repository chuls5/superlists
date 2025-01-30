from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
		self.browser.implicitly_wait(10)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Lisa has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# She types "Buy peacock feathers" into a text box (Lisa's hobby
		# is tying fly-fishing luers)
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list"
		inputbox.send_keys(Keys.ENTER)

		# Wait until the page updates and table contains new row
		WebDriverWait(self.browser, 10).until(
			EC.text_to_be_present_in_element((By.TAG_NAME, 'tr'), '1: Buy peacock feathers')
		)

		table = self.browser.find_elements_by_tag_name('tr')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Lisa is very methodical)
		self.fail('Finish the test!')

		# The page updates again, and now shows both items on her list

		# Lisa wonders whether the site will remeber her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanitory text to that effect.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep


if __name__ == '__main__':
	unittest.main(warnings='ignore')
