from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Käivitab Chrome'i
driver = webdriver.Chrome()

# Avab  lehe
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(2)

# Leiab "Add Element" nupu
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

# Vajutab nuppu 5 korda
for i in range(5):
    add_button.click()
    time.sleep(0.5)

print("5 Delete nuppu on loodud.")

# Leiab kõik Delete nupud
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

print("Delete nuppe leiti:", len(delete_buttons))

# Kustutab kõik Delete nupud
for button in delete_buttons:
    button.click()
    time.sleep(0.5)

print("Kõik Delete nupud on kustutatud.")

# Jätab Chrome'i avatuks
input("Vajuta Enter, et Chrome sulgeda...")

driver.quit()