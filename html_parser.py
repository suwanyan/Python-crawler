# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:10:21 2018

@author: pcpc7-5
"""
#解析器
from bs4 import BeautifulSoup
import re
#import urlparse
import urllib.parse

class HtmlParser(object):
    
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        
        #https://baike.baidu.com/item/Python/407313?fr=aladdin
        links = soup.find_all('a', href=re.compile(r"/item/\d+aladdin"))
        for link in links:
            new_url = link['href']
            #new_full_url = urlparse.urljoin(page_url, new_url)
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
            
    def _get_new_data(self,page_url, soup):
        print('_get_new_data')
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        #soup = BeautifulSoup(html_cont,'html_parser',from_encoding = 'utf-8')
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls ,new_data
        