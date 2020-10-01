Setup Ubuntu 20.04

sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4 libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt --fix-broken install
(You might have to run the dpkg command again if you had to fix broken dependecies)


Python Dependencies
sudo apt install python3-pip
python3 -m pip install pyvirtualdisplay selenium

Install ChromeDriver

wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver