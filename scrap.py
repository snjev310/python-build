from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from webdriver_manager.firefox import GeckoDriverManager
import json
from selenium.webdriver.common.by import By
option = Options()
option.headless = False
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(options=option)
driver.implicitly_wait(5)

url = 'https://www.youtube.com/watch?v=fR9U6--Grng'
driver.get(url)

time.sleep(3)
channel_section = driver.find_element(By.ID,"content-section")
channel_details = channel_section.text.split("\n")
channel_name = channel_details[0]
channel_subscribers = channel_details[1].split(" ")[0]
channel_desc = channel_details[2]
no_of_videos = channel_details[1].split(" ")[1][12:]
print(channel_details)
print(no_of_videos)