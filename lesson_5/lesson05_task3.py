from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера Firefox
driver = webdriver.Firefox()

# Переход на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Поиск текстового поля (на странице всего одно input)
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "Sky"
input_field.send_keys("Sky")

# Очищаем поле
input_field.clear()

# Вводим текст "Pro"
input_field.send_keys("Pro")

# Закрытие браузера
driver.quit()
