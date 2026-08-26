from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Käivitame Chrome'i
driver = webdriver.Chrome()

# Avame avalehe
driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)

# Leiame "Checkboxes" lingi ja klikime
checkboxes_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
checkboxes_link.click()

time.sleep(2)

# Leiame kõik checkboxid
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

print("Checkboxe leiti:", len(checkboxes))

# Märgime mõlemad kastid
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

print("Mõlemad checkboxid on märgitud.")

# Kontrollime tulemust
for i, checkbox in enumerate(checkboxes, start=1):
    print(f"Checkbox {i} märgitud:", checkbox.is_selected())

# Läheme tagasi eelmisele lehele
driver.back()

time.sleep(2)

print("Läksime tagasi avalehele.")

# Jätame Chrome'i avatuks
input("Vajuta Enter, et Chrome sulgeda...")

driver.quit()