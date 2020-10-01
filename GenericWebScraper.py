#!/usr/bin/env python3

import time
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pyvirtualdisplay import Display
import argparse
from dateutil import parser as dateparser
import datetime, time
import sqlite3
import sys
import csv
import multiprocessing as mp
import os, subprocess
import struct
from multiprocessing.pool import ThreadPool
from multiprocessing import Process
import pandas as pd
import shutil


def main():
    parser = argparse.ArgumentParser(description="Generic Web Scraper - Just another web scrapper")
    parser.add_argument("-yt", "--youtube", action="store_true", help="Grab some comments from a Youtube Vide")
    parser.add_argument("-u", "--url", action="store", help="The URL that will be grabbed")
    

data=[]
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s')
for item in range(200): 
    wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
    time.sleep(15)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
    data.append(comment.text)

with Chrome(executable_path="PATH WHERE YOUR DRIVER IS") as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")
for item in range(200): 
    wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
    time.sleep(15)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
    data.append(comment.text)

import pandas as pd   
df = pd.DataFrame(data, columns=['comment'])
df.head()


