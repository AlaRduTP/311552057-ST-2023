from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')

# launch browser
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(15)

# navigate to NYCU home page (https://www.nycu.edu.tw/)
driver.get('https://www.nycu.edu.tw/')
# maximize the window
driver.maximize_window()

# click 新聞
a = driver.find_elements(By.TAG_NAME, 'a')
a = list(filter(lambda x: x.get_attribute('title') == '新聞', a))[0]
a.click()

# click first news
a = driver.find_element(By.XPATH, '//*[@id="-tab"]/ul/li/a')
a.click()

# print the title
print('\n[*] The title of 1st news:\n')
title = driver.find_element(By.XPATH, '//*[@id="content"]/article/header/h1')
print(title.text)

# print the content
print('\n[*] The content of 1st news:\n')
content = driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/p')
content = map(lambda c: c.text, content)
print(*content, sep='\n\n')

# open a new tab and switch to it
driver.switch_to.new_window('tab')
driver.implicitly_wait(15)

# navigate to google (https://www.google.com)
driver.get('https://www.google.com')

# input your student number and submit
i = driver.find_element(By.XPATH, '//*[@name="q"]')
i.send_keys('311552057')
i.send_keys(Keys.ENTER)

# print the title of second result
print('\n[*] The title of 2nd result:\n')
r = driver.find_elements(By.XPATH, '//*[@id="rso"]/div//a/h3')[1]
print(r.text)

# close the browser
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
