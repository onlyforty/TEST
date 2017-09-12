# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class IQIYI:
    '''
    iqiyi网站异步抓取
    '''
    def __init__(self,url):
        self.driver = webdriver.PhantomJS(
            executable_path="/Users/administrator/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
        self.url=url

    #设置浏览器
    def driveweb(self):
        try:
            self.driver.get(self.url)
            self.driver.set_window_size(1000, 3000)
        except Exception, e:
            print e

    #判断是否存在该css选择器 存在返回true 否则返回false
    def get_element(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
            return True
        except:
            return False

    #获取播放量
    def getplaycount(self):
        global count
        if self.get_element('#widget-playcount') == False:
            return 'Null'
        else:
            try:
                count = self.driver.find_element_by_css_selector('#widget-playcount').text

            except Exception, e:
                print e
            for i in range(0, 5, 1):
                if count == '':

                    time.sleep(5)
                    count = self.driver.find_element_by_css_selector('#widget-playcount').text

                else:
                    return count

            else:
                return "TIMEOUT"
    #获取点赞数
    def getvotecount(self):
        global count1
        if self.get_element('#widget-voteupcount') == False:
            return 'Null'
        else:
            try:
                count1 = self.driver.find_element_by_css_selector('#widget-voteupcount').text

            except Exception, e:
                print e

            for i in range(0, 5, 1):
                if count1 == '':

                    time.sleep(2)
                    count1 = self.driver.find_element_by_css_selector('#widget-voteupcount').text

                else:
                    return count1

            else:
                return "TIMEOUT"



    #获取评论数
    def getcomcount(self):

        global count2
        if self.get_element('#qitancommonarea > div:nth-child(2) > div > div > div > div.csPpFeed_hd > ul > li > em > i') == True:
            selector = '#qitancommonarea > div:nth-child(2) > div > div > div > div.csPpFeed_hd > ul > li > em > i'
        elif self.get_element('#qitancommonarea > div:nth-child(2) > div > div > div:nth-child(1) > div.cs-feed-hd > ul > li.selected > em > i')==True:
            selector = '#qitancommonarea > div:nth-child(2) > div > div > div:nth-child(1) > div.cs-feed-hd > ul > li.selected > em > i'

        else:
            return 'mei'
        try:
            count2 = self.driver.find_element_by_css_selector(selector).text

        except Exception, e:
            print e

        for i in range(0, 5, 1):
            if count2 == '':

                time.sleep(3)
                count2 = self.driver.find_element_by_css_selector(selector).text

            else:
                return count2

        else:
            return "TIMEOUT"



    # 获取时间
    def gettime(self):

        global count3
        if self.get_element('#widget-shortrecmd > ul > li.selected > div > div.con-right > p:nth-child(3)') == False:
            return 'Null'
        else:
            try:
                count3 = self.driver.find_element_by_css_selector(
                    '#widget-shortrecmd > ul > li.selected > div > div.con-right > p:nth-child(3)').text

            except Exception, e:
                print e

            for i in range(0, 5, 1):
                if count3 == '':

                    time.sleep(3)
                    count3 = self.driver.find_element_by_css_selector(
                        '#widget-shortrecmd > ul > li.selected > div > div.con-right > p:nth-child(3)').text

                else:
                    return count3

            else:
                return "TIMEOUT"

        #主函数
    def main(self):

        self.driveweb()
        time.sleep(10)
        num={}
        num[0] = self.getplaycount()
        num[1] = self.getvotecount()
        num[2] = self.getcomcount()
        num[3] = self.gettime()
        print u"播放量:" + num[0], u"点赞数:" + num[1], u"评论数:"+ num[2], "时间:" +num[3]
        self.driver.quit()
        return num[0],num[1],num[2]




if __name__ =='__main__':
        iqiyi=IQIYI('http://www.iqiyi.com/v_19rr7kvxuw.html')
        iqiyi.main()



