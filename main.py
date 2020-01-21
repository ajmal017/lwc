from selenium import webdriver
from proxy import proxy_chrome
import time
import pandas as pd
import datetime
import random
import json

def find_ele(text):
    elements = driver.find_elements_by_css_selector(text)
    a = []
    for i in elements:
        print(i.text)
        a.append(i.text)
    return a

def save_site(prox, folder, url):
    driver = proxy_chrome(prox, 12000, auth['username'], auth['password'])
    driver.get(url)
    time.sleep(15)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(folder + '/' + stamp + prox + '.html', 'w') as f:
        f.write(driver.page_source)
    elements = driver.find_elements_by_css_selector('a h3')
    a = []
    for i in elements:
        print(i.text)
        a.append(i.text)
    return a

f = open('../config.json', 'r')
j = f.read()
f.close()
o = json.loads(j)

auth = o['proxy']

stamp = datetime.datetime.now().strftime("%Y-%m-%d")
crowder = 'https://www.google.com/search?ie=UTF-8&q=steven+crowder+youtube&tbm=vid'
gordon = 'https://www.google.com/search?ie=UTF-8&q=gordon+ramsay+youtube&tbm=vid'
joey = 'https://www.google.com/search?ie=UTF-8&q=joe+ingram+youtube&tbm=vid'
proxList = ['manhattan.wonderproxy.com', 
            'london.wonderproxy.com',
            'singapore.wonderproxy.com',
            'toronto.wonderproxy.com', 
            'vienna.wonderproxy.com',
            'zurich.wonderproxy.com']


df = pd.DataFrame(columns=proxList)

for i in proxList:
    df[i] = save_site(i, 'crowder', crowder)
    delay = random.randrange(0,20)
    time.sleep(delay)
df.to_csv('crowder' + stamp + '.csv')

for i in proxList:
    df[i] = save_site(i, 'gordon', gordon)
    delay = random.randrange(0,20)
    time.sleep(delay)
df.to_csv('gordon' + stamp + '.csv')

for i in proxList:
    df[i] = save_site(i, 'joey', joey)
    delay = random.randrange(0,20)
    time.sleep(delay)
df.to_csv('joey' + stamp + '.csv')