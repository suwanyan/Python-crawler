# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:09:08 2018

@author: pcpc
"""
#下载器
#import urllib2 
import urllib.request#3以后的版本

class HtmlDownloader(object):
    
    def download(self,url):
        print('download')
        if url is None:
            return None
        #response = urllib.urlopen(url)
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:#说明请求失败
            return None
        #html =str(response.read(),'utf-8')
        #print(response.read())
        return response.read()#返回下载好的内容
    
    