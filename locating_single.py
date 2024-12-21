from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=1AABSU5XMVHPZ&sprefix=lap%2Caps%2C222&ref=nb_sb_ss_ts-doa-p_2_3")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))
# print(elem.text)

time.sleep(4)
driver.close()