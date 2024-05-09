import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://softekogradecalculator.netlify.app/calculator/grade-calculator?type=percentage")

wait = WebDriverWait(driver, 10)  # Increased wait time
# Wait until the "+ Add new row" button is clickable
add_new_row_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='+ Add new row']"))
)

assignment_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g Assignment']"))
)

# Send a value to this input field
assignment_input.send_keys("Assignment")

Grade_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.0.grade']"))
)

# Send a value to this input field
Grade_input.send_keys("50")

weight_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.0.weight']"))
)

# Send a value to this input field
weight_input.send_keys("100")

project_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g Project']"))
)

# Send a value to this input field
project_input.send_keys("python")

Grade_input1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.1.grade']"))
)

# Send a value to this input field
Grade_input1.send_keys("45")

weight_input1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.1.weight']"))
)

# Send a value to this input field
weight_input1.send_keys("60")
time.sleep(2)

button1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='targeted-container']//div[3]//button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M6.914 4.7')]"))
)

time.sleep(1)
reset_clear = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset/Clear']"))
)


# Attempt to click the button
try:
    add_new_row_button.click()
except Exception as e:
    print("Error clicking the button:", str(e))
    # If normal click fails, try JavaScript click
    driver.execute_script("arguments[0].click();", add_new_row_button)
time.sleep(1)

try:
    button1.click()
except Exception as e:
    print("Error clicking the button:", str(e))
    # If normal click fails, try JavaScript click
    driver.execute_script("arguments[0].click();", button1)

time.sleep(1)


try:
    reset_clear.click()
except Exception as e:
    print("Error clicking the button:", str(e))
    # If normal click fails, try JavaScript click
    driver.execute_script("arguments[0].click();", reset_clear)

# Continue with any other actions or close
input("Press Enter to close...")

driver.quit()
