# -*- coding: utf-8 -*-
from selenium import webdriver
import time



class TENCENT:
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

    # 判断是否存在该css选择器 存在返回true 否则返回false
    def get_element(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
            return True
        except:
            return False
    #获取播放量
    def getplaycount(self):
        global count
        if self.get_element('#mod_cover_playnum') == False:
            return 'Null'
        else:
            try:
                count = self.driver.find_element_by_css_selector('#mod_cover_playnum').text

            except Exception, e:
                print e
            for i in range(0, 5, 1):
                if count == '':

                    time.sleep(5)
                    count = self.driver.find_element_by_css_selector('#mod_cover_playnum').text

                else:
                    return count

            else:
                return "TIMEOUT"



    #获取评论数
    def getcomcount(self):

        global count2
        if self.get_element('#commentTotleNum > span') == False:
            return 'Null'
        else:
            try:

                count2 = self.driver.find_element_by_css_selector('#commentTotleNum > span').text

            except Exception, e:
                print e


            for i in range(0, 5, 1):
                if count2 == '':

                    time.sleep(5)
                    count2 = self.driver.find_element_by_css_selector('#commentTotleNum > span').text

                else:
                    return count2

            else:
                return "TIMEOUT"
    #获取时间
    def gettime(self):
            global count1
            if self.get_element('#fullplaylist > div.player_side_bd > div:nth-child(2) > div > div.mod_playlist > div > div:nth-child(1) > a > div.figure_pic > div > span') == False:
                return 'Null'
            else:
                try:

                    count1 = self.driver.find_element_by_css_selector('#fullplaylist > div.player_side_bd > div:nth-child(2) > div > div.mod_playlist > div > div:nth-child(1) > a > div.figure_pic > div > span').text

                except Exception, e:
                    print e

                for i in range(0, 5, 1):
                    if count1 == '':

                        time.sleep(2)
                        count1 = self.driver.find_element_by_css_selector('#fullplaylist > div.player_side_bd > div:nth-child(2) > div > div.mod_playlist > div > div:nth-child(1) > a > div.figure_pic > div > span').text

                    else:
                        return count1

                else:
                    return "TIMEOUT"


        #主函数
    def main(self):

        self.driveweb()
        time.sleep(5)
        num={}
        num[0] = self.getplaycount()
        num[2] = self.getcomcount()
        num[1] = self.gettime()
        print u"播放量:" + num[0], u"评论数:"+ num[2],u"发布时间：" +num[1]


        self.driver.quit()
        return num[0],num[2]



if __name__ == '__main__':
    tencent = TENCENT('https://v.qq.com/x/cover/c7i7yggth1326oz/o0024bp8grt.html')
    tencent.main()
