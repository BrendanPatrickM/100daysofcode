from selenium import webdriver


path = "/Users/brendan/Development/chromedriver"
selenium = webdriver.Chrome(executable_path=path)

selenium.get('https://en.wikipedia.org/wiki/Main_Page')
article_num = selenium.find_element_by_css_selector('#articlecount a').text

print(article_num)

selenium.quit()
