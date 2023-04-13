from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument('-headless')

# launch browser
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(15)

# Q2-1-1
driver.get('https://docs.python.org/3/tutorial/index.html')

# Q2-1-2
langs = Select(driver.find_elements(By.XPATH, '//*[@id="language_select"]')[1])
langs.select_by_value('zh-tw')

# Q2-1-3
t = driver.find_element(By.XPATH, '//*[@id="the-python-tutorial"]/h1')
p = driver.find_element(By.XPATH, '//*[@id="the-python-tutorial"]/p')
print(t.text)
print(p.text)

i = driver.find_elements(By.XPATH, '//input[@name="q"]')[1]
i.send_keys('class')
i.send_keys(Keys.ENTER)

try:
    e = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="body"]/div[@id="search-results"]/p[@class="search-summary"]'))
    )
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element_value(e, '搜尋完成')
    )
    print(e.text)
except:
    print('timeout!')
