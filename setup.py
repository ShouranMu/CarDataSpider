# -*- coding: UTF-8 -*-
import time
from configobj import ConfigObj
from selenium import webdriver

# read configuration from file "config.ini" section basic
def get_basic_config():
	basic_config = []
	config = ConfigObj("config.ini")
	basic_section = config["basic"]
	basic_config.append(basic_section["homepage"])
	basic_config.append(basic_section["set_update"])
	#print(basic_config)
	return basic_config

# setup the connection and open the index page
def get_homepage(url):
	try:
		option = webdriver.ChromeOptions()
		option.add_argument("headless")
		driver = webdriver.Chrome(chrome_options=option)
		driver = webdriver.Chrome()
		driver.get(url)
		return driver
	except Exception as e:
		return "error"

# need to be more flexible later
def set_configuration(driver):
	# select only public seller
	time.sleep(15)
	driver.find_element_by_id("adLimitation_ONLY_DEALER_ADS").click()
	# public seller with 5 stars
	time.sleep(15)
	driver.find_element_by_id("sr-5-ds").click()
	print("--------------------- 5-star public sellers selected ------------------------")
	return driver
