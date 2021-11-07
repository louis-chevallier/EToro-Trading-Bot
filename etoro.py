# -*- coding: utf-8 -*-
"""etoro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T1MQ8efSrVqc4EO4whuFBC9ppfVTgiq3
"""

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

!apt-get install firefox-geckodriver

! which firefox

!whereis geckodriver
! apt install firefox  xvfb > /dev/null
! pip3 install requests==2.23 folium==0.2.1 pyvirtualdisplay selenium webdriver_manager  > /dev/null

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
    
#wd = browser = webdriver.Firefox(executable_path=    GeckoDriverManager().install())

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
sys.path.insert(0,'/usr/bin')
from selenium import webdriver
#options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()


options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# changing user-agent because etoro detects the automated browser somehow
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/86.0.4240.183 Safari/537.36")
fp = webdriver.FirefoxProfile()
#wd = webdriver.Chrome('chromedriver',options=options)
wd = webdriver.Firefox(executable_path='/usr/bin/firefox', firefox_profile=fp, options=options)
wd.get("https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com")
wd.title

#from google.colab import drive
#drive.mount('/content/drive')

!pwd
#%cd drive/MyDrive/tmp
!ls

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
user = "clovis-heaulier"
pwd = "EToro_35"
driver = wd #webdriver.Firefox()
browser = driver.get("https://www.etoro.com/fr/login")
print(("driver title ", driver.title))
assert "eToro" in driver.title

html_source = browser.page_source

with open("html.html", "w") as fd : fd.write(html_source)

elem = None
try:
    elem = driver.find_element_by_class_name("i-menu-user-username")
except: pass
if (elem!=None) and (elem.text==user): 
  print("logged in")
else:
#assert "Facebook" in driver.title
    print("Logging in...")
    elem = driver.find_element(by=By.ID, value="username")
    elem = driver.find_element_by_id("username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    try:
        wait_ele = EC.presence_of_element_located((By.CLASS_NAME, 'i-menu-user-username'))
        WebDriverWait( browser, 5 ).until(wait_ele)
        elem = driver.find_element_by_class_name("i-menu-user-username")
    except TimeoutException: print("Loading took too much time!")
    except: pass
    if (elem!=None) and (elem.text==user): 
      print("logged in!!")
    else: 
      print("wtf?")
    driver.close()