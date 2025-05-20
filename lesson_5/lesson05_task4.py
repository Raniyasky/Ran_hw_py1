from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера Firefox
driver = webdriver.Firefox()

# Переход на страницу авторизации
driver.get("http://the-internet.herokuapp.com/login")

# Ввод логина
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Ввод пароля
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Нажатие кнопки Login
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()


flash_message = driver.find_element(By.ID, "flash")
print("Сообщение после входа:", flash_message.text.strip())

# Закрытие браузера
driver.quit()