from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_validation():
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:8082")

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        message = driver.find_element(By.ID, "message")

        # Test 1: Empty fields
        button.click()
        assert "Please enter" in message.text

        # Test 2: Incorrect credentials
        username.send_keys("admin")
        password.send_keys("wrong123")
        button.click()
        assert "Invalid" in message.text

        # Test 3: Correct demo credentials
        username.clear()
        password.clear()
        username.send_keys("admin")
        password.send_keys("admin123")
        button.click()
        assert "Login Successful!" in message.text

        print("All login validation tests passed!")

    finally:
        driver.quit()
