import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://softekogradecalculator.netlify.app/calculator/grade-calculator?type=percentage")
time.sleep(10)


def webdriverWait(driver, param):
    pass


wait = webdriverWait(driver, 10)

add_new_row_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='+ Add new row']"))
)

add_new_row_button.click()
