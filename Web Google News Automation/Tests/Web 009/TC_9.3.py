import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click Language and region
driver.find_element(By.XPATH,'//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[7]/span/div').click()
time.sleep(3)
#type bangla in search box
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[11]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/input').send_keys("Bangla")
time.sleep(1)
#select first language
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[11]/div[2]/div/div[1]/div/div[2]/ul/li[76]/div/div').click()
time.sleep(2)
#click update button
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[11]/div[2]/div/div[2]/button[2]').click()
time.sleep(3)
driver.close()
driver.quit()
print("Pass")