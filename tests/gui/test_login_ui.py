from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_page_title():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    assert "The Internet" in driver.title

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    welcome_text = driver.find_element(By.TAG_NAME, "h2").text
    assert "Secure Area" in welcome_text
    driver.quit()

