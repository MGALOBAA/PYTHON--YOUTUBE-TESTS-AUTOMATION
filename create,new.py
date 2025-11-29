from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Open browser
driver = webdriver.Chrome()

# Step 2: Go to Facebook
driver.get("https://www.facebook.com")

# Step 3: Click "Create new account"
create_account_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Create new account"))
)
create_account_btn.click()

# Step 4: Wait for signup form to appear and fill details
firstname = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "firstname"))
)
firstname.send_keys("Giorgi")

lastname = driver.find_element(By.NAME, "lastname")
lastname.send_keys("QA Tester")

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("giorgi.test@example.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("TestPassword123")

# Step 5: Select date of birth
driver.find_element(By.NAME, "birthday_day").send_keys("10")
driver.find_element(By.NAME, "birthday_month").send_keys("May")
driver.find_element(By.NAME, "birthday_year").send_keys("1995")

# Step 6: Select gender (1 = Female, 2 = Male, -1 = Custom)
driver.find_element(By.XPATH, "//input[@value='2']").click()  # Male

# Step 7: Click Sign Up button
signup_btn = driver.find_element(By.NAME, "websubmit")
signup_btn.click()

# Wait a little to see result
time.sleep(5)

# Close browser (optional)
driver.quit()
   