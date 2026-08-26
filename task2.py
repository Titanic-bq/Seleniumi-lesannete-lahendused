from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Käivitame Chrome'i
driver = webdriver.Chrome()

# Avame tsitaatide lehe
driver.get("https://quotes.toscrape.com")

# Anname lehele aega laadida
time.sleep(2)

# Leiame kõik tsitaadid
quotes = driver.find_elements(By.CLASS_NAME, "text")

# Leiame kõik autorid
authors = driver.find_elements(By.CLASS_NAME, "author")

# Prindime tsitaadid koos autoritega
for quote, author in zip(quotes, authors):
    print("Tsitaat:", quote.text)
    print("Autor:", author.text)
    print()

# Jätame brauseri avatuks
input("Vajuta Enter, et Chrome sulgeda...")

driver.quit()