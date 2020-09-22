import os
import function as insta_public
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
def main():
        File='url.txt'
        File1='hashtags.txt'
        nooflinks=2
        noofhashtags=2
        noofimages=100
        browser='firefox'
        chag='hashtag'
        username=''
        password=''
        user=str(username)
        password=str(password)
        if browser=='chrome':
            driver = webdriver.Chrome() 
        elif browser=='firefox':
            driver=webdriver.Firefox()
        time.sleep(2)
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        driver.find_element_by_name('username').send_keys(user)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        time.sleep(8)
        if chag=='link':
            for i in range(0,nooflinks):
                with open(File) as Links:
                    Link = Links.readlines()[i]
                    changedir(i,chag)
                    insta_public.download(Link,driver,i)
                    os.chdir('C:/Users/Mustafa/Desktop/fiver project/Instagram-Downloader-Selenium-master')
        elif chag=='hashtag':
            for j in range(0,noofhashtags):
                with open(File1) as Links:
                    hashtag = Links.readlines()[j]
                    Link='https://www.instagram.com/explore/tags/'+hashtag
                    changedir(j,chag)
                    insta_public.download(Link,driver,j,noofimages)
                    os.chdir('C:/Users/Mustafa/Desktop/fiver project/Instagram-Downloader-Selenium-master')

def changedir(hashtag,chag):
    while(FileExistsError):
        hashtag+=1
        directory='C:/Users/Mustafa/Desktop/fiver project/Instagram-Downloader-Selenium-master/#'+str(hashtag)
        try:
            os.mkdir(directory)
            print("Directory " , directory ,  " Created ")
        except(FileExistsError):
            print("already existed")           
if __name__ == "__main__":
    main()