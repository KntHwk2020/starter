from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf4j1pcO4W4agA2xAPx8Z783qlWSf1M2rGRCBEt01AnoF5cKw/viewform?usp=pp_url')

time.sleep(2)

#To get xpath, open webdeveloper tools on site and click on the field, then choose copy then xpath
first_name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
first_name.send_keys('Ace')


last_name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last_name.send_keys('Masterson')


time.sleep(3)

submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
submit.click()