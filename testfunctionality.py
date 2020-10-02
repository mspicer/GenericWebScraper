#!/usr/bin/env python3

#exec(open("./testfunctionality.py").read())

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
author=[]
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=un9x-DjTMT0')
wait = WebDriverWait(driver,15)
df = pd.DataFrame()

for item in range(10): 
    wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
    time.sleep(2)
# for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#ytd-comment-renderer"))):
#     #author.append(comment.text)    
#     df = df.append({'author': author}, ignore_index=True))
df = pd.concat([pd.DataFrame([author.text], columns=['Author']) for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )], ignore_index=True)

df['AuthorLink'] = [author.get_attribute('href') for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )]

df['Comment'] = [comment.text for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text")) )]

# for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
#     data.append(comment.text)

print(df.head())