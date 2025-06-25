from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0")
driver = webdriver.Chrome(options=options)

driver.get("https://www.olx.in/items/q-car-cover")
time.sleep(7)

ads = driver.find_elements(By.TAG_NAME, "li")
results = []
for ad in ads:
    try:
        title = ad.find_element(By.TAG_NAME, "h6").text.strip()
        link = ad.find_element(By.TAG_NAME, "a").get_attribute("href")
        results.append(f"{title}\n{link}\n")
    except:
        continue

with open("car_cover_olx_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results) if results else "No listings found.")

driver.quit()
print("Saved listings to car_cover_olx_results.txt")
print(f"Total listings found: {len(results)}")
