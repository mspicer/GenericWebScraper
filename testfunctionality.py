#!/usr/bin/env python3

import time
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pyvirtualdisplay import Display
import pandas as pd

data=[]
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s')
wait = WebDriverWait(driver,15)
for item in range(5): 
    wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
    time.sleep(15)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
    data.append(comment.text)
