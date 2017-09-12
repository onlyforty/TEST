# -*- coding: utf-8 -*-

import re
import requests
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    '''
    从初始url开始，寻找所有匹配所给正则的url
    '''

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.links1 = []


    def handle_starttag(self,tag,attrs):
        #输出开头标签为a
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for(variable,value) in attrs:
                    if variable == "href":
                        self.links.append(value)
    @staticmethod
    def get_code(url):
        # 获取网页源代码
        wb_data = requests.get(url)
        return wb_data.text

    @staticmethod
    #匹配正则url
    def match(content,url):
        pattern = re.compile(url)
        item = re.match(pattern, content)
        if item != None:
            return content
        else:
            pass

    #获取新的链接
    def get_links(self,url,reurl):
     html_code = MyHTMLParser.get_code(url)
     hp = MyHTMLParser()
     hp.feed(html_code)
     for i in range(0,len(hp.links)):
       if MyHTMLParser.match(hp.links[i],reurl)==None:
           continue
       else:
           self.links1.append(hp.links[i])
     hp.close()
     return self.links1
if __name__ == "__main__":
         parser=MyHTMLParser()
         parser.get_links('http://sports.iqiyi.com/','http://www.iqiyi.com/v_.*.html')

