#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:21:40 2019

@author: olivia
"""
#

from bs4 import BeautifulSoup
from selenium import webdriver
import os, inspect
import pandas as pd
#%%
def open_browser(path):
    '''
    1. Check documentation with: help(open_browser) or open_browser.__doc__
    2. Headless Chrome in AWS:
    https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/
    
    Define a selenium webdriver with headless Chrome.
    
    Headless Chrome is shipping in Chrome 59. It's a way to run the Chrome browser 
    in a headless environment. Essentially, running Chrome without chrome! It brings
    all modern web platform features provided by Chromium and the Blink rendering 
    engine to the command line.
    
    Why is that useful?
    A headless browser is a great tool for automated testing and server environments
    where you don't need a visible UI shell. For example, you may want to run some 
    tests against a real web page, create a PDF of it, or just inspect how the 
    browser renders an URL.
    '''
    chrome_path = path # full path of the chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage');
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.add_experimental_option("prefs",prefs)    
    driver = webdriver.Chrome(executable_path = chrome_path,
                              options=chrome_options) 
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30000)
    return driver

def get_info(browser_path=None, URL=None, num_of_data=None):
    '''
    use selenium to get data
    1. get source data
    2. define soup
    3. extract useful data
    '''
    driver = open_browser(path=browser_path)
    driver.get(URL)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    UG_list_b = soup.find_all(name="div", attrs={"class":"UG_list_b"})
    
    # scroll down until get enough data
    while len(UG_list_b)<num_of_data:
        print(f"<--------------- No of articles : {len(UG_list_b)}")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        UG_list_b = soup.find_all(name="div",attrs={"class":"UG_list_b"})
        
#    driver.quit()
            
    # process data extraction
#    links = ["https:" + item for item in UG_list_b[2]]
#    list_des = [item for item in UG_list_b.find(name="div",attrs={"class":"list_des"})]
#    articles = [item for item in list_des.find(name='h3',attrs={"class":"list_title_s"}).getText()]
#    subinfo = [item for item in list_des.find(name="div",attrs={"class":"subinfo_box clearfix"})] 
#    dt = [item for item in subinfo.find_all(name="span",attrs={"class":"subinfo S_txt2"})[1].getText()]
#    likesp = [item for item in subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[0]] 
#    likes = [item for item in likesp.find_all(name="em")[1].getText()] 
#    viewsp = [item for item in subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[2]]
#    views = [item for item in viewsp.find_all(name="em")[1].getText()]
    
    links=[]
    articles=[]
    dt=[]
    likes=[]
    views = []
    for item in soup.find_all(name="div",attrs={"class":"UG_list_b"}):
        link = "https:" + item['href']
        links.append(link)
        
        list_des = item.find(name="div",attrs={"class":"list_des"})
        article = list_des.find(name="h3",attrs={"class":"list_title_s"}).getText()
        articles.append(article)
 
        subinfo = list_des.find(name="div",attrs={"class":"subinfo_box clearfix"}) 
        dati = subinfo.find_all(name="span",attrs={"class":"subinfo S_txt2"})[1].getText()
        dt.append(dati)

        likesp = subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[0] 
        like = likesp.find_all(name="em")[1].getText() 
        likes.append(like)
 
        viewsp = subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[2] 
        view = viewsp.find_all(name="em")[1].getText()
        views.append(view)

    df_articles = pd.DataFrame(columns = ["article_content", "datetime", "views", "likes", "links"])
    df_articles['article_content'] = articles
    df_articles['datetime'] = dt
    df_articles['views'] = views
    df_articles['likes'] = likes
    df_articles['links'] = links
    print(df_articles)
    
    df_articles.to_json(os.path.join(BASE, "weibo.json"), orient="index")
    
    return df_articles
    
#%%
BASE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) #changable
browser_path = os.path.join(BASE, "chromedriver") #changable
URL = "https://www.weibo.com/sg"  #changable
get_info(browser_path=browser_path, URL=URL, num_of_data=100)
#driver = open_browser(path=browser_path)
#driver.get(URL)

#%%
#links=[]
#articles=[]
#dt=[]
#likes=[]
#views=[]
#
#for item in soup.find_all(name="div",attrs={"class":"UG_list_b"}):
#    link = "https:" + item['href']
#    links.append(link)
#    print(link)
#    
#    list_des = item.find(name="div",attrs={"class":"list_des"})
#    article = list_des.find(name="h3",attrs={"class":"list_title_s"}).getText()
#    articles.append(article)
#    print(article)
#    
#    subinfo = list_des.find(name="div",attrs={"class":"subinfo_box clearfix"}) 
#    dati = subinfo.find_all(name="span",attrs={"class":"subinfo S_txt2"})[1].getText()
#    dt.append(dati)
#    print(dati)
#    
#    likesp = subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[0] 
#    like = likesp.find_all(name="em")[1].getText() 
#    likes.append(like)
#    print(like)
#    
#    viewsp = subinfo.find_all(name="span",attrs={"class":"subinfo_rgt S_txt2"})[2] 
#    view = viewsp.find_all(name="em")[1].getText()
#    views.append(view)
#    print(view)
#
#df_articles = pd.DataFrame(columns = ["article_content", "datetime", "views", "likes", "links"])
#df_articles['article_content'] = articles
#df_articles['datetime'] = dt
#df_articles['views'] = views
#df_articles['likes'] = likes
#df_articles['links'] = links
#print(df_articles)
#
#df_articles.to_json(os.path.join(BASE, "weibo.json"), orient="index")






