import time

import pyautogui

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://store.steampowered.com/")
element = driver.find_element(By.XPATH, "//a[@class='tab  '][contains(@href,'points')]")
element.click()
time.sleep(3)

driver.get("https://store.steampowered.com/")
element = driver.find_element(By.XPATH, "//a[@class='tab  '][contains(@href,'news')]")
element.click()
time.sleep(3)


driver.get("https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header")
element = driver.find_element(By.XPATH, "//input[@id='input_username']")
element.send_keys("ya_karal")
element = driver.find_element(By.XPATH, "//input[@id='input_password']")
element.send_keys("gj[eq,kzlbyf")
element = driver.find_element(By.XPATH, "//button")
element.click()
time.sleep(3)

driver.get("https://store.steampowered.com/")
mouse = driver.find_element("link text", 'Категории')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(0.5)
driver.find_element("link text", 'Экшен').click()
time.sleep(5)

driver.get("https://store.steampowered.com/")
element = driver.find_element(By.XPATH, "//input[@id='store_nav_search_term']")
element.send_keys("dota")
element.submit()
time.sleep(5)

driver.get("https://store.steampowered.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='home_cluster_ctn home_ctn']/div/div/div[@class='arrow right']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='home_cluster_ctn home_ctn']/div/div/div[@class='arrow right']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='home_cluster_ctn home_ctn']/div/div/div[@class='arrow right']").click()
time.sleep(5)

driver.close()
