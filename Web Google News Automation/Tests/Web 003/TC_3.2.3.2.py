import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to headlines
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span").click()

time.sleep(3)
#first headlines select
title = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article")
time.sleep(2)
#more icon locator
moreIcon = driver.find_element(By.XPATH,'//*[@id="tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ"]/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/span[2]')
#hover => title => Share icon
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(moreIcon).perform()
time.sleep(3)
#more icon click
moreIcon.click()
time.sleep(2)
#go to link click
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div/div/span[2]/div[3]/div/div").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()

