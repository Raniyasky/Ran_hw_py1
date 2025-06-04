import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_test.login_page import LoginPage
from shop_test.products_page import ProductsPage
from shop_test.cart_page import CartPage
from shop_test.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total_price(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    products_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    products_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    products_page.go_to_cart()
    cart_page.click_checkout()

    checkout_page.fill_info("Рания", "Халиуллина", "420000")
    total = checkout_page.get_total()

    assert total == "$58.29"
