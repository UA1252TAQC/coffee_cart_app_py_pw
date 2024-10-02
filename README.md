# coffee_cart_app_py_pw
https://coffee-cart.app/

## Installation and Running

1. Create a virtual environment:
	```sh
	python -m venv venv
	```

2. Activate the virtual environment:
	- On Windows:
		```sh
		.\venv\Scripts\activate
		```
	- On macOS/Linux:
		```sh
		source venv/bin/activate
		```

3. Install dependencies:
	```sh
	pip install -r requirements.txt
	```

4. Create a [`.env`](.env) file in the root of your project with the following content:
	```plaintext
	BASE_URL=
	```

5. Run tests:
	```sh
	pytest
	```
