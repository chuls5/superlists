import time
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

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element(By.ID, 'id_list_table')
		rows = table.find_elements(By.TAG_NAME, 'tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Lisa visits the home page
		self.browser.get('http://localhost:8000')

		# She checks the title and header
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
		self.assertIn('To-Do', header_text)

		# She enters a to-do item
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# She types "Buy peacock feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')


		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list"
		inputbox.send_keys(Keys.ENTER)


		# Wait for the new entry to appear
		WebDriverWait(self.browser, 10).until(
			EC.text_to_be_present_in_element((By.ID, 'id_list_table'), 'Buy peacock feathers')
		)
		self.check_for_row_in_list_table('1: Buy peacock feathers')


		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Lisa is very methodical)
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)


		# Wait for the second entry to appear
		WebDriverWait(self.browser, 10).until(
			EC.text_to_be_present_in_element((By.ID, 'id_list_table'), 'Use Peacock feathers to make a fly')
		)


		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Lisa wonders whether the site will remeber her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanitory text to that effect.
		self.fail('Finish the tests!')
		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep


if __name__ == '__main__':
	unittest.main(warnings='ignore')
