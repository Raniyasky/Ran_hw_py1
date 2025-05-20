from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/classattr")

# Нахождение синей кнопки по части класса (btn-primary)
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Клик по кнопке
button.click()

# Закрыть браузер
driver.quit()