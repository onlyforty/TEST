# -*- coding: utf-8 -*-
import requests
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from IQIYI_crawler import IQIYI
from TENCENT_crawler import TENCENT
from YOUKU_crawler import YOUKU

class Save_video:
    '''
    抓取该url下所需的元素并存入数据库
    '''
    def __init__(self,url):
        #url初始化
        self.url = url


    def get_code(self):
        # 获取网页源代码
        try:
         wb_data = requests.get(self.url)
         wb_data.encoding='utf-8'
        except Exception ,e:
         print e
        return wb_data.text

    def match_web(self):
        #根据url判断属于哪个视频网站
        if re.search("iqiyi.com", self.url):
            return 'iqiyi'
        else:
            if re.search("v.qq.com", self.url):
                return 'tencent'
            else:
                if re.search("v.youku.com", self.url):
                    return 'youku'


    def get_ele(self):
        #获取页面元素
        a=self.match_web()
        if a=='iqiyi':
            iqiyi = IQIYI(self.url)
            playnum,praisenum,comnum=iqiyi.main()
            webname = '爱奇艺'

        else:
            if a=='tencent':
                tencent = TENCENT(self.url)
                playnum,  comnum = tencent.main()
                praisenum='Null'
                webname = '腾讯视频'
            else:
                if a=='youku':
                    youku = YOUKU(self.url)
                    playnum, praisenum, comnum=youku.main()
                    webname = '优酷视频'
                else:
                    playnum, praisenum, comnum,webname='Null','Null','Null','Null'
        code =self.get_code()
        soup = BeautifulSoup(code, "lxml")
        try:
         # if soup.select("#widget-videotitle"):
         #   title = soup.select("#widget-videotitle")[0].get_text()
         if soup.title:
             title = soup.title.text

         else:
            title = 'Null'
         print title
         if soup.select("#widget-vshort-ptime"):
             pubdate = soup.select("#widget-vshort-ptime")[0].get_text()[5:]
         else:
             pubdate = 'Null'
         createtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
         #if  soup.select("#datainfo-navlist > a"):
         # webname = soup.select("#datainfo-navlist > a")[0].get_text()
         #else:
          #   webname='Null'
        except Exception,e:
            print e
        return title,pubdate,createtime,webname,self.url,code,playnum,praisenum,comnum

    def getconn(self,host,user,password,database):
      #连接数据库  参数依次为服务器，用户名，密码，数据库名
      try:
       conn = mysql.connector.connect(host=host,user=user, password=password, database=database)
       print "数据库连接成功"
      except Exception:
          print "数据库连接失败"
      return conn

    def save_database(self):
        #入库
        conn = self.getconn("localhost","root","","webcrawler")
        cursor=conn.cursor()
        #查询是否已存在该url
        query1 = "SELECT COUNT(*) FROM `t_video` WHERE `url`='%s' "  %self.url
        cursor.execute(query1)
        num = cursor.fetchone()
        print num[0]


        #不存在的话 插入数据
        if num[0] >= 1:
          print "已存在该数据"

        else:
         query2 = """SELECT `id` FROM `t_video` ORDER BY `id` DESC LIMIT 0,1"""
         cursor.execute(query2)
         id = cursor.fetchone()[0]+1

         title, pubdate, createtime, webname, url ,code,playnum,praisenum,comnum= self.get_ele()
         #print code
         values =(id,1,'Null',title,'Null',code,'Null',url,webname,pubdate,createtime,createtime,playnum,praisenum,comnum)
         # 插入data表
         try:
          query = """INSERT INTO `t_video`(`id`, `srcId`, `keyword`, `title`, `brief`, `text`, `sourceText`, `url`,
               `webName`, `pubDate`, `createtime`, `updateTime`, `playnum`, `praisenum`, `comnum`) VALUES (%s,%s,%s,%s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s)"""
          cursor.execute(query, values)
          print "成功插入数据库"
          conn.commit()
          cursor.close()
          conn.close
         except Exception,e:
            print e

if __name__== "__main__":
     a=Save_video('https://v.qq.com/x/cover/kv79rr6d2qo1rnc.html?videoMark=')
     a.save_database()