# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:14:22 2018

@author: pcpc 7-3
"""
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#待爬取URL
        self.old_urls = set()#已经爬取过的URL
        
    def add_new_url(self,url):#添加新的URL
        print('add_new_url')
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#
            self.new_urls.add(url)
    
    def add_new_urls(self,urls):#添加
        print('add_new_urls')
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):#判断管理器中是否有待爬取URL
        print('has_new_url')
        return len(self.new_urls) !=0
    
    def get_new_url(self):#从URL管理器中获取一个新的待爬取URL
        print('get_new_url')
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    