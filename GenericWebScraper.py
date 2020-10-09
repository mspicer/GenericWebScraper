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
# import sqlite3
import sys
import csv
# For future use:
# import multiprocessing as mp
# import os, subprocess
# import struct
# from multiprocessing.pool import ThreadPool
# from multiprocessing import Process
# import shutil
import pandas as pd
from urllib.parse import urlparse
from sqlalchemy import create_engine
import re

VERBOSE = False

def main():
    global VERBOSE
    parser = argparse.ArgumentParser(description="Generic Web Scraper - Just another web scrapper")
    parser.add_argument("-yt", "--youtube", action="store_true", dest='youtube', help="Grab some comments from a Youtube Video")
    parser.add_argument("-cc", "--comment_count", action="store", dest="cmcnt", help="The number of pages of comments to get")
    parser.add_argument("-u", "--url", action="store", dest='url', help="The URL that will be grabbed")
    parser.add_argument("-db", "-db_out", action="store_true", dest="dbout", help="Output the data to SQLite.")
    parser.add_argument("-c", "--csv", action="store_true", dest="csv", help="Output the data as CSV file")
    parser.add_argument("-o", "--out_file", action="store", dest="output", help="Output file")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Make things verbose")
    parser.add_argument("-fs", "--find_search", action="store_true", dest="findsearch", help="Search for the search functionality and return what it")

    args = parser.parse_args()
    
    if args.verbose:
        VERBOSE = True

    if args.url:
        pr = urlparse(args.url)
        if pr.scheme == '' and pr.netloc == '':
            usage(parser)
            sys.exit(1)
    filename = "scrape-{}".format(int(time.time()))
    if args.output:
        filename = args.output

    if args.url and args.youtube and args.cmcnt:
        grabytcomments(args.url, cnt=args.cmcnt)
    elif args.url and args.youtube:
        d = grabytcomments(args.url)
        if VERBOSE:
            print("Record Count: {}".format(len(d.index)))
        if len(d.index) > 0 and args.dbout:
            #Convert dataframe to sqlite db
            engine = create_engine("sqlite:///{}".format(filename), echo=True)
            sqlite_connection = engine.connect()
            d.to_sql('ytcomments', sqlite_connection)
        if len(d.index) > 0 and args.csv:
            d.to_csv(filename)
        else:
            for row in d:
                print(row)
    elif args.findsearch and args.url:
        findsearch(args.url)
    


def usage(parser):
    print("""
++++++++++++++++++++++++++++++
    Generic Web Scraper
++++++++++++++++++++++++++++++
""")
    parser.print_help()
    sys.exit(1)

def grabytcomments(url, cnt=10):
    global VERBOSE
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver,15)
    df = pd.DataFrame()


    for item in range(int(cnt)): 
        if VERBOSE:
            print("Sending END key, iteration: {}".format(item))
        wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
        time.sleep(2)

    df = pd.concat([pd.DataFrame([author.text], columns=['Author']) for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )], ignore_index=True)
    if VERBOSE:
        print("Authors added to dataframe, Count: {}".format(df.count()))

    df['AuthorLink'] = [author.get_attribute('href') for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text")) )]
    if VERBOSE:
        print("Authors profile link added to dataframe, Count: {}".format(df.count()))

    df['Comment'] = [comment.text for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text")) )]
    if VERBOSE:
        print("Comment added to dataframe, Count: {}".format(df.count()))
    print(df.head())
    return df

def findsearch(url):
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    mo = re.search("<form.*search.*>", driver.page_source)
    print(mo.group())
    s = mo.group()
    #print(s.find('method'))
    mpos = s.find('method')
    method = s[mpos+8:s.find('\"', mpos+8)-1]
    apos = s.find('action')
    action = s[apos+8:s.find('\"', apos+8)-1]
    print("Action: {} Method: {}".format(action, method))
    # res = [i.start() for i in re.finditer('search', driver.page_source)]
    # for l in res:
    #     print(driver.page_source[l:driver.page_source.find("\n", l)])
    
if __name__ == "__main__":
    main()