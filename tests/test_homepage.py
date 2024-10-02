from pages.homepage import HomePage

def test_homepage_title(page):
	homepage = HomePage(page)
	homepage.goto("https://coffee-cart.app/")
	assert homepage.get_title() == "Coffee cart"

def test_homepage_title2(page):
	homepage = HomePage(page)
	homepage.goto("https://coffee-cart.app/")
	assert homepage.get_title() == "Coffee cart1"