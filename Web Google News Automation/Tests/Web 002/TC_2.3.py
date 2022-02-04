import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#find search box
driver.find_element(By.XPATH, "//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]").send_keys("narrow search")
driver.find_element(By.CLASS_NAME, "gb_gf").click()

time.sleep(3)
#find narrow search
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div/article/a").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()
