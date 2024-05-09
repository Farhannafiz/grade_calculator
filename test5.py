import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the test result counters
pass_count = 0
fail_count = 0

# Function to print results based on assertions or checks
def print_result(status, message):
    global pass_count, fail_count
    print(f"======{status}===== {message}")
    if status == "PASS":
        pass_count += 1
    else:
        fail_count += 1

# Set up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the target page
driver.get("https://softekogradecalculator.netlify.app/calculator/grade-calculator?type=percentage")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Loop to repeat the process 10 times
for i in range(10):
    # Find "+ Add new row" button
    try:
        add_new_row_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='+ Add new row']"))
        )
        print_result("PASS", f"Add New Row button found on iteration {i + 1}")
    except Exception as e:
        print_result("FAIL", f"Add New Row button not found on iteration {i + 1}: {str(e)}")

    # Input assignment and project values
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

    time.sleep(1)

    # Click "+ Add new row" button
    try:
        add_new_row_button.click()
        print_result("PASS", f"Successfully clicked Add New Row button on iteration {i + 1}")
    except Exception as e:
        print_result("FAIL", f"Error clicking Add New Row button on iteration {i + 1}: {str(e)}")
        driver.execute_script("arguments[0].click();", add_new_row_button)

    # Check if a new row was added
    try:
        row_added = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='targeted-container']//div[contains(@class, 'row-container') and contains(text(), 'Assignment')]"))
        )
        print_result("PASS", f"New row was successfully added on iteration {i + 1}")
    except Exception as e:
        print_result("FAIL", f"New row was not added on iteration {i + 1}: {str(e)}")

    # Click the "Reset/Clear" button and verify clearing fields
    reset_clear = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset/Clear']"))
    )
    try:
        reset_clear.click()
        # Verify that fields are cleared (basic assertion to see if inputs are empty)
        assert assignment_input.get_attribute("value") == "", "Assignment field not cleared"
        assert grade_input.get_attribute("value") == "", "Grade field not cleared"
        assert weight_input.get_attribute("value") == "", "Weight field not cleared"
        assert project_input.get_attribute("value") == "", "Project field not cleared"
        print_result("PASS", f"Successfully clicked Reset/Clear button and cleared fields on iteration {i + 1}")
    except AssertionError as e:
        print_result("FAIL", f"Fields not cleared after Reset/Clear on iteration {i + 1}: {str(e)}")
    except Exception as e:
        print_result("FAIL", f"Error clicking Reset/Clear button on iteration {i + 1}: {str(e)}")
        driver.execute_script("arguments[0].click();", reset_clear)

# Print the summary of test results
print(f"\nTotal tests run: {pass_count + fail_count}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")

# Wait for the user to inspect the results and then close the browser
input("Press Enter to close...")
driver.quit()
