from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Нахождение синей кнопки по части класса (btn-primary)
button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")

# Клик по кнопке
button.click()

# Закрыть браузер
driver.quit()