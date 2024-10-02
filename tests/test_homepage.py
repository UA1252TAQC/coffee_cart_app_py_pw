from pages.homepage import HomePage
from utils.config import get_base_url

def test_homepage_title(page):
	homepage = HomePage(page)
	homepage.goto(get_base_url())
	assert homepage.get_title() == "Coffee cart"

def test_homepage_menu_items(page):
	homepage = HomePage(page)
	homepage.goto(get_base_url())
	menu_items = homepage.get_menu_items()
	assert len(menu_items) > 0

def test_homepage_menu_item_price(page):
	homepage = HomePage(page)
	homepage.goto(get_base_url())
	price = homepage.get_menu_item_price("Espresso")
	assert price == "$10.00"

def test_homepage_checkout(page):
	homepage = HomePage(page)
	homepage.goto(get_base_url())
	homepage.click_checkout()
	total = homepage.get_checkout_total()
	assert total == "Total: $0.00"