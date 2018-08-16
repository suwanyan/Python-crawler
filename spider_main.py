# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:26:43 2018

@author: pcpc
"""
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()#url管理器
        self.downloader = html_downloader.HtmlDownloader()#下载器
        self.parser = html_parser.HtmlParser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#输出器
        
    def craw(self,root_url):#爬虫调度程序
        count=1
        self.urls.add_new_url(root_url)#添加一个URL
        while self.urls.has_new_url():#当URL管理器中有待爬取URL时
           # try:
           new_url=self.urls.get_new_url()#获取一个待爬取URL
           html_cont=self.downloader.download(new_url)#启动下载器下载页面
           print ("craw %d : %s"%(count,new_url))
           new_urls,new_data=self.parser.parse(new_url,html_cont)#解析URL和数据
           self.urls.add_new_urls(new_urls)#添加进URL管理器
           self.outputer.collect_data(new_data)#收集数据
           if count == 1000:
               break
           count=count+1
          #  except:
            #  print ("craw faild")  
            
        self.outputer.output_html()#输出页面数据          
       
if __name__=="__main__":
    print('1')
    root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"#入口URL
    obj_spider=SpiderMain()#启动爬虫
    obj_spider.craw(root_url)
    print('2')