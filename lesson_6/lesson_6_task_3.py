from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Явное ожидание: загрузка картинки с id="award"
wait = WebDriverWait(driver, 15)
image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img#award")))

# Получение src
image_src = image.get_attribute("src")
print("SRC картинки с id='award':", image_src)

# Закрытие браузера
driver.quit()
