from selenium import webdriver  
import time


path = "/Users/brendan/Development/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

print(item_ids)

while True:
    cookie.click()
    if time.time() > timeout:
        points = driver.find_element_by_id('money')
        for class in item_ids:
            


        timeout = time.time() + 5


<div id="buyCursor" onclick="Buy('Cursor');" style="background-image:url(cursoricon.png);" class=""><b>Cursor - <moni></moni> 17</b>Autoclicks every 5 seconds.<div class="amount">1</div></div>
