#!/usr/bin/env python
# coding: utf-8

# In[275]:
#import pandas as pd
import requests
import os, inspect
from time import sleep
from bs4 import BeautifulSoup
#import selenium
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


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
#     chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage');
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.add_experimental_option("prefs",prefs)    
    driver = webdriver.Chrome(executable_path = chrome_path,
                              options=chrome_options) 
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30000)
    return driver


def login_web(driver=None, URL=None, uname=None, pwd=None):
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'lxml')
#    get_start_pre = soup.find(name="div", attrs={"class":"bk u bl"})
    driver.find_element_by_link_text("Get started").click()
    sleep(1)
    driver.find_element_by_link_text("Sign up with Google").click()
    sleep(1)
    driver.find_element_by_tag_name("input").send_keys(uname) #uname
    driver.find_element_by_tag_name("input").submit()
    driver.find_element_by_id("identifierNext").click()
    sleep(3)
    driver.find_element_by_name("password").send_keys(pwd) #pwd
    driver.find_element_by_name("password").submit()
    driver.find_element_by_id("passwordNext").click()
    sleep(3)
    driver.get(URL)
    sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    return soup

def search_fun(driver=None, soup=None, kwd=None, data_no=None):
    search_func = soup.find(name = 'div', attrs = {'class':"buttonSet buttonSet--wide"})
    search_src = search_func.find(name='a',attrs={'class':'button button--small button--chromeless u-sm-show is-inSiteNavBar u-baseColor--buttonNormal button--withIcon button--withSvgIcon button--chromeless u-xs-top1'})['href']
    driver.get(search_src)
    sleep(2)
#    soup_s = BeautifulSoup(driver.page_source, 'lxml')
#    search_page = soup_s.find(name="form",attrs={"class":"js-searchForm"})
    driver.find_element_by_tag_name("input").send_keys(kwd)
    driver.find_element_by_tag_name("input").submit()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sleep(5)
    postArticle = soup.find_all(name="div",attrs={"class":"postArticle-readMore"})
    while len(postArticle)<data_no:
    #     assert len(postArticle)>0
        print(f"<--------------- No of articles : {len(postArticle)}")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        soupSoup = BeautifulSoup(driver.page_source, 'html.parser')
        postArticle = soupSoup.find_all(name="div",attrs={"class":"postArticle-readMore"})
    return postArticle
# In[277]:


# set path 
BASE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
browser_path = os.path.join(BASE, "chromedriver")
URL = "https://medium.com"

driver = open_browser(path=browser_path)

soup = login_web(driver=driver, URL=URL, uname="olivia19931019@gmail.com", pwd="Zhous_8875")

postArticle = search_fun(driver=driver, soup=soup, kwd="machine learning", data_no=20)
article_links = [article.find(name="a")["href"] for article in postArticle]
article_soups = [BeautifulSoup(requests.get(url).content, features="lxml") for url in article_links]
#%%
#article_titles = [title.find(name="title").getText() for title in article_soups]
#article_authors = [author.find(name="meta", attrs={"name":"author"})['content'] for author in article_soups]
#article_content = [p.getText() for p in article_soups[i].find_all(name="p") for i in range(len(article_soups))]

articles = [
        {
                "title":article_soup.find(name="title").getText(),
                "author":article_soup.find(name="meta", attrs={"name":"author"})['content'],
                "content":[p.getText() for p in article_soup.find_all(name="p")]
                } for article_soup in article_soups
        ]