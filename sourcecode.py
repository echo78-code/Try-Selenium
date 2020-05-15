from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import TimeoutException

print('Please enter your username')
username_user = input()
print('Please enter your password')
password_user = input()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
username_field = driver.find_element_by_name("username")
username_field.clear()
username_field.send_keys(username_user)

password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys(password_user)

driver.find_element_by_id("login-button").send_keys(Keys.ENTER)

try:
    WebDriverWait(driver,10).until(cond.visibility_of_element_located((By.CLASS_NAME,'RootlistItem__link')))
    content = driver.find_elements_by_class_name('RootlistItem__link')
    print('Found ' + str(len(content)) + ' Playlists in your profile')
    for i in range(len(content)):
         b = content[i].text
         print(str(i+1) + ' - ' + b)
    a = int(input())
    content[a-1].click()
    time.sleep(5)
    driver.find_element_by_class_name('_11f5fc88e3dec7bfec55f7f49d581d78-scss').send_keys(Keys.ENTER)

    n = 0
    while(1):
        print('Enter 1 to exit the player')
        n = int(input())
        if(n==1):
            break
finally:
    driver.quit()
