from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# 1. Запуск браузера и переход на страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

wait = WebDriverWait(driver, 15)
# дождаться, пока загрузится поле «First name»
wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

@pytest.fixture(scope="module")
def func():
    # 2. Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # zip-code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # 3. Отправка формы
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. Ожидание появления сообщений об ошибках/успешности
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.alert")))

@pytest.mark.parametrize(["id", "result"],[
    ("first-name","alert-success"),
    ("last-name","alert-success"),
    ("address","alert-success"),
    ("e-mail","alert-success"),
    ("phone","alert-success"),
    ("city","alert-success"),
    ("country","alert-success"),
    ("job-position","alert-success"),
    ("company","alert-success"),
    ("zip-code","alert-danger"),
    ])
def test_first_name(id, result, func):
    element_class_attribute = driver.find_element(By.ID, id).get_attribute("class")
    assert result in element_class_attribute
