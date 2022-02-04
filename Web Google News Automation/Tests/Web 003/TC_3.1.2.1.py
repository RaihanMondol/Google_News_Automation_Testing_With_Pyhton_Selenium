import time

import pyperclip


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#find search box
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span").click()

time.sleep(3)
#find headlines
a=driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]/span/div").click()

time.sleep(3)
#copy headlines link
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div[2]/div/div/div[3]/div[2]/div[1]").click()
#paste link which copy from clipboard
link = pyperclip.paste()
#create new tab
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
#open the link wchich is copied
driver.get(link)
time.sleep(3)
print("Pass")
time.sleep(5)
driver.close()
driver.quit()

