_author_ = 'gbinod'
from selenium import webdriver
import bs4
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

dr = webdriver.Chrome(chrome_options=chrome_options)

dr.maximize_window()
dr.get('http://172.18.40.156/solr/#/programs')
time.sleep(10)
source = bs4.BeautifulSoup(dr.page_source, 'lxml')
optimized = source.find('dd', {'class': 'index_optimized'})
optimized = optimized.find('span')
current = source.find('dd', {'class': 'index_current'})
current = current.find('span')
print(optimized.text)
print(current.text)
dr.close()


