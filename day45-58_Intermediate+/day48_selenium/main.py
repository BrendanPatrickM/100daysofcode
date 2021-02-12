from selenium import webdriver
chrome_driver_path = "/Users/brendan/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://www.python.org')
events_tag = driver.find_elements_by_css_selector('.medium-widget.event-widget .shrubbery ul li')

events = [item.text for item in events_tag]
print(events)

driver.quit()


