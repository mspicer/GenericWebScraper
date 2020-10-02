#!/usr/bin/env python3

'''
Generic Web Scraper
By: Mike Spicer (@d4rkm4tter)
'''

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
from urllib.parse import urlparse

def main():
    parser = argparse.ArgumentParser(description="Generic Web Scraper - Just another web scrapper")
    parser.add_argument("-yt", "--youtube", action="store_true", dest='youtube', help="Grab some comments from a Youtube Vide")
    parser.add_argument("-c", "--comment_count", action="store", dest="cmcnt", help="The number of pages of comments to get")
    parser.add_argument("-u", "--url", action="store", dest='url', help="The URL that will be grabbed")
    
    args = parser.parse_args()
        
    if args.url:
        pr = urlparse(args.url)
        if pr.scheme == '' and pr.netloc == '':
            usage(parser)
            sys.exit(1)

    if args.url and args.youtube and args.cmcnt:
        grabytcomments(args.url, cnt=args.cmcnt)
    elif args.url and args.youtube:
        grabytcomments(args.url)
    


def usage(parser):
    print("""
++++++++++++++++++++++++++++++
    Generic Web Scraper
++++++++++++++++++++++++++++++
""")
    parser.print_help()
    sys.exit(1)

def grabytcomments(url, cnt=10):

    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver,15)
    df = pd.DataFrame()


    for item in range(int(cnt)): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
        time.sleep(2)

    df = pd.concat([pd.DataFrame([author.text], columns=['Author']) for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )], ignore_index=True)

    df['AuthorLink'] = [author.get_attribute('href') for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )]

    df['Comment'] = [comment.text for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text")) )]
    print(df.head())

    
if __name__ == "__main__":
    main()