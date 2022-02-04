import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#send feedback
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[11]/span/div/span').click()
#select feedback option and write feedback
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/uf-describe-page/form/div[1]').send_keys("Thank you")
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/uf-describe-page/form/footer/uf-material-button[1]/label/button').click()

time.sleep(10)
driver.close()
driver.quit()
print("Pass")