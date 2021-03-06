# -*- coding: utf-8 -*-
from selenium import webdriver
import time



class YOUKU:
    '''
    优酷网异步数据抓取
    '''
    def __init__(self,url):
        self.driver = webdriver.PhantomJS(
            executable_path="/Users/administrator/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs",
                )
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
        if self.get_element('#videoTotalPV > em') == False:
            return 'Null'
        else:
            try:
                count = self.driver.find_element_by_css_selector('#videoTotalPV > em').text

            except Exception, e:
                print e
            for i in range(0, 5, 1):
                if count == '':

                    time.sleep(5)
                    count = self.driver.find_element_by_css_selector('#videoTotalPV > em').text

                else:
                    return count

            else:
                return "TIMEOUT"

            # 获取点赞数
    def getvotecount(self):
        global count1
        if self.get_element('#upVideoTimes') == False:
            return 'Null'
        else:
            try:
                count1 = self.driver.find_element_by_css_selector('#upVideoTimes').text

            except Exception, e:
                print e

            for i in range(0, 5, 1):
                if count1 == '':

                    time.sleep(5)
                    count1 = self.driver.find_element_by_css_selector('#upVideoTimes').text

                else:
                    return count1

            else:
                return "TIMEOUT"

    #获取评论数

    def getcomcount(self):

        global count2
        if self.get_element('#videocomment > div.comment-tab > ul.comment-tab-left > li.current.comment-show') == False:
            return 'TIMEOUT'
        else:
            try:
                ele = self.driver.find_element_by_css_selector('#videocomment > div.comment-tab > ul.comment-tab-left > li.current.comment-show')
                ele.click()
                count2 = self.driver.find_element_by_css_selector('#allCommentNum').text

            except Exception, e:
                print e

            for i in range(0, 5, 1):
                if count2 == '':
                    time.sleep(5)

                    count2 = self.driver.find_element_by_css_selector('#allCommentNum').text

                else:
                    return count2

            else:
                return "TIMEOUT"


        #主函数
    def main(self):

        self.driveweb()

        time.sleep(5)
        num={}
        num[0] = self.getplaycount()
        num[1] = self.getvotecount()
        if self.getcomcount()=='TIMEOUT':
            num[2] = self.getcomcount()
        else:
            num[2] = self.getcomcount()[1:-1]
        print u"播放量:" + num[0], u"点赞数:" + num[1], u"评论数:"+ num[2]

        self.driver.quit()
        return num[0],num[1],num[2]




if __name__ == '__main__':
    youku = YOUKU('http://v.youku.com/v_show/id_XMjk3MDY3Njc2OA==.html?spm=a2hww.20023042.m_223465.5~5~5~5!3~5~5~A&f=50716895')
    youku.main()
