# Generic Web Scraper

## Description

This project is a collection of scraping methods that I thought were cool using Selenium and Chrome core. This helps with dynamically loading content that is using AJAX or web sockets to show information. The goal of this project is to build scraper tech generically that will for a wide array of applications. 

## Usage

  -h, --help            show this help message and exit
  -yt, --youtube        Grab some comments from a Youtube Video
  -cc CMCNT, --comment_count CMCNT
                        The number of pages of comments to get
  -u URL, --url URL     The URL that will be grabbed
  -db, -db_out          Output the data to SQLite.
  -c, --csv             Output the data as CSV file
  -o OUTPUT, --out_file OUTPUT
                        Output file
  -v, --verbose         Make things verbose


## Setup Ubuntu 20.04

sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4 libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt --fix-broken install
(You might have to run the dpkg command again if you had to fix broken dependecies)

Python Dependencies
sudo apt install python3-pip
python3 -m pip install pyvirtualdisplay selenium pandas sqlalchemy

Install ChromeDriver

wget https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

sudo rm /usr/bin/chromedriver
sudo rm /usr/local/bin/chromedriver