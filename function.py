import requests
from bs4 import BeautifulSoup as bs
import time
from time import sleep
import requests as req
import os
import json
import sys
import re
def download(url,driver,dir,images):
    num=0
    driver.get(url)
    time.sleep(3)
    SCROLL_PAUSE_TIME = 1
    images_unique=[]
    last_height = driver.execute_script("return document.body.scrollHeight")
    if images<=33:
        num=1
    elif images<=45 and images>33:
        num=2
    elif images<=57 and images>45:
        num=3
    elif images<=69 and images>57:
        num=4
    elif images<=81 and images>69:
        num=5
    elif images<=93 and images>81:
        num=6
    elif images<=105 and images>93:
        num=7
    elif images<=117 and images>105:
        num=8
    elif images<=129 and images>117:
        num=9
    elif images<=141 and images>129:
        num=10
    elif images<=153 and images>141:
        num=11
    elif images<=165 and images>153:
        num=12
    elif images<=177 and images>165:
        num=13
    elif images<=189 and images>177:
        num=14
    elif images<=201 and images>189:
        num=15
    elif images<=213 and images>201:
        num=16
    elif images<=225 and images>213:
        num=17
    else:
        num=25
    while True:
        if num>0:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            num-=1
            time.sleep(SCROLL_PAUSE_TIME)
            time.sleep(4)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
                break
            last_height = new_height
            time.sleep(4)
            html_to_parse=str(driver.page_source)
            html=bs(html_to_parse,"html5lib")
            images_url=html.findAll("img", {"class": "FFVAD"})
            in_first = set(images_unique)
            in_second = set(images_url)
            in_second_but_not_in_first = in_second - in_first
            result = images_unique + list(in_second_but_not_in_first)
            images_unique=result
        else:
            break
    directory='C:/Users/Mustafa/Desktop/fiver project/Instagram-Downloader-Selenium-master/#'+str(dir)
    os.chdir(directory)
    for i in range(0,images):
        name="image"+str(i)+".jpg"
        print(name)
        with open(name, 'wb') as handler:
            try:
                img_data = requests.get(images_unique[i].get("src")).content
                handler.write(img_data)
            except:
                print("Slow internet")
                try:
                    img_data = requests.get(images_unique[i].get("src")).content
                    handler.write(img_data)
                except:
                    print("Retrying Again")
                    try:
                        img_data = requests.get(images_unique[i].get("src")).content
                        handler.write(img_data)
                    except:
                        print("VERY VERY SLOW Internet")
                        img_data = requests.get(images_unique[i].get("src")).content
                        handler.write(img_data)

                
    return