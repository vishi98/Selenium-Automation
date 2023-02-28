from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

MAIL = 'mail'
PWD = 'password'

s = Service("C:/bin/chromedriver.exe")
o = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=o)

driver.get('https://tinder.com/app/recs')
time.sleep(2)
login_btn = driver.find_element(By.CLASS_NAME, 'button')
login_btn.click()
time.sleep(1)
login_fb = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_fb.click()
time.sleep(2)
tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(1)
mail = driver.find_element(By.XPATH, '//*[@id="email"]')
mail.send_keys(GMAIL)
pwd = driver.find_element(By.XPATH, '//*[@id="pass"]')
pwd.send_keys(PWD)
login_btn = driver.find_element(By.ID, 'loginbutton')
login_btn.submit()
driver.switch_to.window(tinder_window)
time.sleep(6)
tinder_ok = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
tinder_ok.click()
tinder_msg = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
tinder_msg.click()
while True:
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except:
        print("error")
        driver.quit()