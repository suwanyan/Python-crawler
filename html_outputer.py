# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:12:04 2018

@author: pcpc
"""

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        #ascil
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")   
        
        fout.write("<table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close