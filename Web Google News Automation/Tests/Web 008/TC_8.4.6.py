import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click business button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[7]/a'). click()
time.sleep(3)
#click Entrepreneurship
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[6]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")