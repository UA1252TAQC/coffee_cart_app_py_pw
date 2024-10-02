from .base_page import BasePage

class HomePage(BasePage):
	def __init__(self, page):
		super().__init__(page)
		self.title_selector = "title"

	def get_title(self):
		return self.page.title()