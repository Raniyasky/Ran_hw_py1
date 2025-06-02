import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для драйвера, работает на весь модуль
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Функция выполняет шаги по заданию
def web_calculator_with_delay(driver, delay_param, num1_param, num2_param, operation_param):
    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Ввод задержки
    input_delay = driver.find_element(By.ID, "delay")
    input_delay.clear()
    input_delay.send_keys(str(delay_param))

    # 3. Нажатие первой цифры
    for digit in str(num1_param):
        driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{digit}']").click()

    # 4. Нажатие операции
    driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{operation_param}']").click()

    # 5. Нажатие второй цифры
    for digit in str(num2_param):
        driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{digit}']").click()

    # 6. Нажатие =
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='=']").click()

    # 7. Ожидание результата
    screen = driver.find_element(By.CSS_SELECTOR, "div.screen")
    initial_text = screen.text

    WebDriverWait(driver, delay_param + 5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "div.screen").text != initial_text
    )

    # 8. Получение и возврат результата
    return driver.find_element(By.CSS_SELECTOR, "div.screen").text

# Параметризация для автотеста
@pytest.mark.parametrize(
    "delay_param, num1_param, num2_param, operation_param, expected_result",
    [(45, 7, 8, '+', 15)]
)
def test_web_calculator_with_expectation(driver, delay_param, num1_param, num2_param, operation_param, expected_result):
    result = web_calculator_with_delay(driver, delay_param, num1_param, num2_param, operation_param)
    assert result == str(expected_result), f"Ожидалось {expected_result}, но получено {result}"
