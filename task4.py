from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Käivitab Chrome'i
driver = webdriver.Chrome()

# Avab login-lehe
driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Leiab kasutajanime välja
username = driver.find_element(By.ID, "username")

# Leiab parooli välja
password = driver.find_element(By.ID, "password")

# Sisestame andmed
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Leiame Login nupu ja klikime
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(2)

# Kontrollib, kas õnnestus
message = driver.find_element(By.ID, "flash").text
# Motivatsioon kiri
if "You logged into a secure area!" in message:
    print("TEST ÕNNESTUS!")
else:
    print("TEST EBAÕNNESTUS!")

print("Sõnum:", message)

# Jätab brauseri avatuks
input("Vajuta Enter, et Chrome sulgeda...")

driver.quit()