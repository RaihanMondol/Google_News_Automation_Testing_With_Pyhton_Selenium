import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click help
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[12]/a/div[1]/span').click()

time.sleep(10)
driver.close()
driver.quit()
print("Pass")