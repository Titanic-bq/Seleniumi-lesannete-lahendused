from selenium import webdriver
import time

# Käivitame Chrome'i
driver = webdriver.Chrome()

# Avab Google'i otsingutulemused Seleniumiga
driver.get("https://www.google.com/search?q=Hendrik+Jürgenson")

# Annab lehele aega laadida
time.sleep(5)

# Screenishoti tegemine otsingutulemustest
driver.save_screenshot("minu_otsing.png")

print("Otsing tehtud!")
print("Screenshot salvestatud: minu_otsing.png")

# Avatud lehe sulgemiseks ootame kasutaja sisendit
input("Vajuta Enter, et Chrome sulgeda...")

driver.quit()