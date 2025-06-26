import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_test.calc_page import CalcPage  # путь к твоему Page Object

# Фикстура
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест
@pytest.mark.parametrize(
    "delay, num1, num2, op, expected",
    [(45, 7, 8, '+', 15)]
)
def test_calc_operation(driver, delay, num1, num2, op, expected):
    page = CalcPage(driver)
    page.open()
    page.set_delay(delay)
    page.click_button(num1)
    page.click_operator(op)
    page.click_button(num2)
    page.click_equals()
    result = page.get_result(timeout=delay+5)
    assert result == str(expected), f"Ожидалось {expected}, получено {result}"
