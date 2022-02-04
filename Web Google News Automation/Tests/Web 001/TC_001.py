from _ast import Assert

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

assert driver.title == "Google News", "Title doesn't match"
print("Pass")
driver.close()
driver.quit()
