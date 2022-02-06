# Google_News_Automation_Testing_With_Pyhton_Selenium
### Given excel file : https://github.com/RaihanMondol/Google_News_Automation_Testing_With_Pyhton_Selenium/tree/main/Web%20Google%20News%20Automation/Given%20excel%20file <br><br><br>
# Web 001
## TC_001
1. Open browser
2. Type url of the taxrise in search bar
3. Press Enter 


```python
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

```
# Web 002
## TC_2.1
1. Click on Search.
2. Go to Featured topic
3. Click any topic from Featured topic


```python
import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#find search box
driver.find_element(By.XPATH, "//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]").send_keys("Featured topic News")
driver.find_element(By.CLASS_NAME, "gb_gf").click()

time.sleep(3)
#find any of news
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div/article/a").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_2.2
1. Click on Search.
2. Go to in the news
3. Click any topic from latest news


```python
import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#find search box
driver.find_element(By.XPATH, "//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]").send_keys("latest news")
driver.find_element(By.CLASS_NAME, "gb_gf").click()

time.sleep(3)
#find latest of news
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div/article/a").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_2.3
Narrow search


```python
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

```
# Web 003
## TC_3.1.1
1. Click on Headlines
2. Click on Follow from the top right 


```python
import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click headlines
driver.find_element(By.XPATH,"//*[@id='i44']/div[1]/h2/span/a").click()

time.sleep(3)
#click follow button
driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[1]/div").click()
#sign in
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div[2]/div/div[2]/div").click()
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("perfectb06@gmail.com")
driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()




```

## TC_3.1.2.1
1. Click on Headlines
2. Click on Share
3. Click on Copy link
4. Create a new tab and pest the link


```python
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


```

## TC_3.1.2.2
1. Click on Headlines
2. Click on Share
3. Click on Facebook.
4. Go to facebook page


```python
import time

import pyperclip


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#search headlines
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span").click()

time.sleep(3)
#find headlines
a=driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]/span/div").click()

time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div[2]/div/div/div[3]/div[2]/div[2]").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()

```

## TC_3.1.2.3
1. Click on Headlines
2. Click on Share
3. Click on Twitter.
4. Go to twitter page


```python
import time

import pyperclip


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click headlines
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span").click()

time.sleep(3)
#find headlines
a=driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]/span/div").click()

time.sleep(3)
#click twitter
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[12]/div[2]/div/div/div[3]/div[2]/div[3]").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_3.2.1
1. Mouse poin to the news tital
2. News tital show the Save for later
3. Click on Save for later icone


```python
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
```

## TC_3.2.2.1
1. Mouse poin to the news tital
2. News tital show the Share
3. Click on share icone
4. Click on Copy link
5. Create a new tab and pest the link


```python
import time

import pyperclip


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to headlines
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span"). click()

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


```

## TC_3.2.2.2
1. Mouse poin to the news tital
2. News tital show the Share
3. Click on share icone
4. Click on Facebook.
5. Go to facebook page


```python
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
#share icon locator
shareIcon = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/span[1]/div")
#hover => title => Share icon
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(shareIcon).perform()
time.sleep(3)
#share icon click
shareIcon.click()
time.sleep(2)
#facebook link click
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[2]').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_3.2.2.3
1. Mouse poin to the news tital
2. News tital show the Share
3. Click on share icone
4. Click on Twitter.
5. Go to twitter page


```python
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
#share icon locator
shareIcon = driver.find_element(By.XPATH,"//*[@id='tabCAQqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURWcWFHY1NBbVZ1R2dKVlV5Z0FQAQ']/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/span[1]/div")
#hover => title => Share icon
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(shareIcon).perform()
time.sleep(3)
#share icon click
shareIcon.click()
time.sleep(2)
#twitter link click
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[3]').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_3.2.3.1
1. Mouse poin to the news tital
2. News tital show the more icone
3. Click on more
4. Click on view full coverage


```python
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
#view full coverage link click
driver.find_element(By.LINK_TEXT,"View Full Coverage").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_3.2.3.2
1. Mouse poin to the news tital
2. News tital show the more icone
3. Click on more
4. Click on Go to .... page link


```python
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


```

## TC_3.2.3.3
1. Mouse poin to the news tital
2. News tital show the more icone
3. Click on more
4. Click on More stories like this


```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to headlines
driver.find_element(By.XPATH, "//*[@id='i45']/div[1]/h2/span"). click()

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
#hide link click
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[13]/div/div/span[3]/div[3]/div/div").click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()


```

## TC_3.3.1
1. Go to the weather part
2. Click on C 



```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to weather in celcius
celcius = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[1]/button').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()



```

## TC_3.3.2
1. Go to the weather part
2. Click on F


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to weather in farenheit
celcius = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[2]').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()



```

## TC_3.3.3
1. Go to the weather part
2. Click on K


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to weather in kelvin
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[3]').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()



```

## TC_3.3.4
1. Go to the weather part
2. Click on More on weather.com


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click to weather in celcius
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/small/a').click()

print("Pass")
time.sleep(5)
driver.close()
driver.quit()



```
# Web 004
## TC_4.1
1. Go to the Beyond the headlines 
2. Mouse poin to the news tital
3. News tital show the Save for later
4. Click on Save for later icone


```python
import time
import pyperclip
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")
#click for you button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[2]'). click()
time.sleep(3)
#headlines locator
title = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/div/main/div/c-wiz/div[1]/div[2]/div/div/article/a')
time.sleep(3)
#save for later icon locator
saveIcon = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/div/main/div/c-wiz/div[1]/div[2]/div/div/article/div/menu/div')
time.sleep(3)
#mouse hover perform
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(saveIcon).perform()
time.sleep(3)
#mouse hover selected element click
saveIcon.click()

print("Pass")
time.sleep(3)
driver.close()
driver.quit()



```

## TC_4.2.1
1. Click on For you from left side
2. Mouse poin to the news tital
3. News tital show the Share
4. Click on share icone
5. Click on Copy link
6. Create a new tab and pest the link


```python
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


```
# Web 005
## TC_5.1
Topics & sources


```python
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click following button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[3]'). click()
#click topics & sources
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div/div[1]/div[2]/div[1]').click()

print("Pass")
time.sleep(3)
driver.close()
driver.quit()

```

## TC_5.2
Saved searches


```python
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click following button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[3]'). click()
#saved searches
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div/div[1]/div[2]/div[2]').click()

print("Pass")
time.sleep(3)
driver.close()
driver.quit()

```

## TC_5.3
Saves stories


```python
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click following button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[3]'). click()
#saved searches
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div/div[1]/div[2]/div[3]').click()

print("Pass")
time.sleep(3)
driver.close()
driver.quit()

```
# Web 006
## TC_006
Saved searches


```python
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click saved searches button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[4]'). click()

print("Pass")
time.sleep(3)
driver.close()
driver.quit()

```
# Web 007
## TC_7.1.1
1. Click on Covid-19 from left side
2. Mouse poin to the news tital
3. News tital show the Save for later
4. Click on Save for later icone


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click covid 19
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[2]/a'). click()
time.sleep(3)
#headlines locator
title = driver.find_element(By.XPATH,'//*[@id="tabCAQqEAgAKgcICjCcuZcLMI_irgMwpbnMBg"]/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div[2]/article[1]')
time.sleep(3)
#save for later icon locator
saveIcon = driver.find_element(By.XPATH,'//*[@id="tabCAQqEAgAKgcICjCcuZcLMI_irgMwpbnMBg"]/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div[2]/article[1]/div/menu/div')
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
```

## TC_7.2.1
1. Click on Covid-19 from left side
2. Click on Local
3. Select location from suggested location


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click covid 19
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[2]/a'). click()
time.sleep(3)
#click local
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[2]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_7.3.1
1. Click on Covid-19 from left side
2. Click on International
3. Select region from suggested region


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click covid 19
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[2]/a'). click()
time.sleep(3)
#click International
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[3]/span/div/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```
# Web 008
## TC_8.1.1
1. Click on US from left side
2. Mouse poin to the news tital
3. News tital show the Save for later
4. Click on Save for later icone


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click USA
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[4]'). click()
time.sleep(1)
#headlines locator
title = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article')
time.sleep(3)
#save for later icon locator
saveIcon = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/div')
time.sleep(1)
#mouse hover perform
actions = webdriver.ActionChains(driver).move_to_element(title).move_to_element(saveIcon).perform()
time.sleep(3)
#mouse hover selected element click
saveIcon.click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.2.1
1. Click on World from left side
2. Mouse poin to the news tital
3. News tital show the Save for later
4. Click on Save for later icone


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click World
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[5]'). click()
time.sleep(3)
#headlines locator
title = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/h3/a')
time.sleep(3)
#save for later icon locator
saveIcon = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div/article/div/menu/div')
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
```

## TC_8.3.1
1. Click on Your location news from left side
2. Select any suggest location


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click Search location
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[6]'). click()
time.sleep(3)
#click first suggession locator
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[1]/span').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.1
Latest


```python
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click business button
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[7]/a'). click()
time.sleep(3)

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.2
Economy


```python
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
#click Economy
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[2]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.3
Markets


```python
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
#click Markets
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[3]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.4
Jobs


```python
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
#click Jobs
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[4]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.5
Personal Finance


```python
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
#click Personal Finnance
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[1]/div[2]/div[5]/span/div').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_8.4.6
Enterpreneurship


```python
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
```
# Web 009
## TC_9.1
1. Click on Language & region from the lest side
2. Search any language.


```python
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

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_9.2
1. Click on Language & region from the lest side
2. For cencel the pop up click cencel on the pop up.


```python
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
#type Bangla in search box
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[11]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/input').send_keys("Bangla")
#click cancel button
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[11]/div[2]/div/div[2]/button[1]').click()

```

## TC_9.3
1. Click on Language & region from the lest side
2. Select any language.
3. Click update.


```python
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
```
# Web 010
## TC_10.1
1. Click on Settings from the lest side
2. Click on manage


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click setting
driver.find_element(By.XPATH,'//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[8]').click()
time.sleep(3)
#click => hidden sources => manage button
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/div/div/div[1]/div[2]/div').click()
time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_10.2
1. Click on Settings from the lest side
2. Click on View.


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click setting
driver.find_element(By.XPATH,'//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[8]').click()
time.sleep(3)
#click => my activity => view button
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/div/div/div[1]/div[3]/div/a').click()
time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```

## TC_10.3
1. Click on Settings from the lest side
2. Click on Dark them box.
3. Select any one from three ( Default, Always, Never)


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click setting
driver.find_element(By.XPATH,'//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[8]').click()
time.sleep(3)
#click dark theme option
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/div/div/div[1]/div[4]/div/div/div/div[1]').click()
#select dark theme option to allways
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/div/div/div[1]/div[4]/div/div/div/div[2]/ul/li[2]').click()
time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```
# Web 011
## TC_011
1. Click on Get the android app from the lest side


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

#click get the android app
driver.find_element(By.XPATH,'//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[9]/a/div[1]/span').click()

time.sleep(3)
driver.close()
driver.quit()
print("Pass")
```
# Web 012
## TC_012
1. Click on Get the iOS app from the lest side


```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:/Web/Google News/Drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en/")

# click get the iOS app
driver.find_element(By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[10]/a/div[1]/span').click()

time.sleep(10)
driver.close()
driver.quit()
print("Pass")
```
# Web 013
## TC_013
1. Click on Send feedback from the lest side
2. Type some thing
3. Click cencel/send


```python
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
```
# Web 014
## TC_014
1. Click on Help from the lest side


```python
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
```
