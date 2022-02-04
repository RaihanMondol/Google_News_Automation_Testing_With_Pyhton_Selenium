import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/foryou?hl=en-US&gl=US&ceid=US%3Aen")

time.sleep(3)
#first headlines select
title = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article")
time.sleep(2)
#share icon locator
shareIcon = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/span[1]/div")
#hover => title => Share icon
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(shareIcon).perform()
time.sleep(3)
#share icon click
shareIcon.click()
time.sleep(2)
#copy link click
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[1]').click()
time.sleep(2)
#paste copy link
link = pyperclip.paste()
#create a nie tab
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
#open the link wchich is copied
driver.get(link)

print("Pass")
time.sleep(5)
driver.close()
driver.quit()

