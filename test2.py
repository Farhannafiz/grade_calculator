import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the target page
driver.get("https://softekogradecalculator.netlify.app/calculator/grade-calculator?type=percentage")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Loop to repeat the process 100 times
for i in range(100):
    # Add a new assignment
    add_new_row_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='+ Add new row']"))
    )

    assignment_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g Assignment']"))
    )
    assignment_input.clear()
    assignment_input.send_keys(f"Assignment {i + 1}")

    grade_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.0.grade']"))
    )
    grade_input.clear()
    grade_input.send_keys("50")

    weight_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.0.weight']"))
    )
    weight_input.clear()
    weight_input.send_keys("100")

    project_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='e.g Project']"))
    )
    project_input.clear()
    project_input.send_keys(f"Project {i + 1}")

    grade_input1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.1.grade']"))
    )
    grade_input1.clear()
    grade_input1.send_keys("45")

    weight_input1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='rows.1.weight']"))
    )
    weight_input1.clear()
    weight_input1.send_keys("60")

    # Wait a short while between iterations
    time.sleep(1)

    # Click the "+ Add new row" button
    try:
        add_new_row_button.click()
    except Exception as e:
        print(f"Error clicking the Add New Row button on iteration {i + 1}: {str(e)}")
        driver.execute_script("arguments[0].click();", add_new_row_button)

    # Click the reset/clear button if required
    reset_clear = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset/Clear']"))
    )
    try:
        reset_clear.click()
    except Exception as e:
        print(f"Error clicking the Reset/Clear button on iteration {i + 1}: {str(e)}")
        driver.execute_script("arguments[0].click();", reset_clear)

# Wait for the user to inspect the results and then close the browser
input("Press Enter to close...")
driver.quit()
