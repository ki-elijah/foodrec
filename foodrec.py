from selenium import webdriver
import time

browser = webdriver.Firefox(exceutable_path='/geckodriver')
browser.get('https://www.caloriemama.ai/api')

upload = find_element_by_class_name('file-upload')
upload.send_keys("/joseph.jpg")

time.sleep(5)

get = browser.find_element_by_class_name('group-name')
print(get.text)