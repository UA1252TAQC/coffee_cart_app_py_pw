from .base_page import BasePage

class HomePage(BasePage):
	def __init__(self, page):
		super().__init__(page)
		self.page = page

	def goto(self, url):
		self.page.goto(url)

	def get_title(self):
		return self.page.title()

	def get_menu_items(self):
		return self.page.query_selector_all("//ul[@data-v-a9662a08]/li/h4")

	def get_menu_item_price(self, item_name):
		return self.page.query_selector(f"//h4[contains(text(), '{item_name}')]/small").inner_text()

	def click_checkout(self):
		self.page.click("//button[@data-test='checkout']")

	def get_checkout_total(self):
		return self.page.query_selector("//button[@data-test='checkout']").inner_text()