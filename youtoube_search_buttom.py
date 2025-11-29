from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open browser
driver = webdriver.Chrome()

# Step 2: Go to YouTube
driver.get("https://www.youtube.com")

# Step 3: Type a word in search box
driver.find_element(By.NAME, "search_query").send_keys("GEORGI TBILISI")

# Step 4: Wait 1 second (so search button becomes active)
time.sleep(1)

# Step 5: Click the search button using its ID
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/button").click()

# Step 6: Wait for the search results to load
time.sleep(3)

# Step 7: Click the first video in the list
driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]").click()






