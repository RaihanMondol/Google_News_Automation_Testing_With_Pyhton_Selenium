import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")


driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span").click()
time.sleep(3)
#headlines locator
title = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article")
time.sleep(3)
#save for later icon locator
saveIcon = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/div")
time.sleep(3)
#mouse hover perform
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(saveIcon).perform()
time.sleep(3)
#mouse hover selected element click
saveIcon.click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")