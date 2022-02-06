import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click headlines
driver.find_element(By.XPATH,"//*[@id='i44']/div[1]/h2/span/a").click()

time.sleep(3)
#click follow button
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[1]/div").click()
#sign in
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div[2]/div/div[2]/div").click()
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("raihanmondolbd@gmail.com")
driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()

