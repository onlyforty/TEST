# -*- coding: utf-8 -*-

from HTMLPARSER import MyHTMLParser
from save_video import Save_video

class MyCrawler:
    '''
    抓取启动主程序
    '''
    def __init__(self, seeds):

        # 使用种子初始化url队列
        self.linkQuence = linkQuence()
        if isinstance(seeds, str):
            self.linkQuence.addUnvisitedUrl(seeds)
        if isinstance(seeds, list):
            for i in seeds:
                self.linkQuence.addUnvisitedUrl(i)
        print "Add the seeds url \"%s\"  to the unvisited url list" % str(self.linkQuence.unVisited)

    # 抓取过程主函数
    def crawling(self, reurl):

            # 循环条件：待抓取的链接不空
            while not self.linkQuence.unVisitedUrlsEnmpy():
                # 队头url出队列
                visitUrl = self.linkQuence.unVisitedUrlDeQuence()
                print "Pop out one url \"%s\" from unvisited url list" % visitUrl
                if visitUrl is None or visitUrl == "":
                    continue
                #存储该url下所需元素
                save=Save_video(visitUrl)
                save.save_database()
                # 获取新的链接
                parser = MyHTMLParser()
                links = parser.get_links(visitUrl,reurl)
                print "Get %d new links" % len(links)
                # 将url放入已访问的url中
                self.linkQuence.addVisitedUrl(visitUrl)
                print "Visited url count: " + str(self.linkQuence.getVisitedUrlCount())
                # 未访问的url入列
                for link in links:
                 self.linkQuence.addUnvisitedUrl(link)
                print "%d unvisited links" % len(self.linkQuence.getUnvisitedUrl())




class linkQuence:
    def __init__(self):
        # 已访问的url集合
        self.visted = []
        # 待访问的url集合
        self.unVisited = []

    # 获取访问过的url``````````````````````````````````````````````````````````````````````````````队列
    def getVisitedUrl(self):
        return self.visted

    # 获取未访问的url队列
    def getUnvisitedUrl(self):
        return self.unVisited

    # 添加到访问过得url队列中
    def addVisitedUrl(self, url):
        self.visted.append(url)

    # 移除访问过得url
    def removeVisitedUrl(self, url):
        self.visted.remove(url)

    # 未访问过得url出队列
    def unVisitedUrlDeQuence(self):
        try:
            return self.unVisited.pop()
        except:
            return None

    # 保证每个url只被访问一次
    def addUnvisitedUrl(self, url):
        if url != "" and url not in self.visted and url not in self.unVisited:
            self.unVisited.insert(0, url)

    # 获得已访问的url数目
    def getVisitedUrlCount(self):
        return len(self.visted)

    # 获得未访问的url数目
    def getUnvistedUrlCount(self):
        return len(self.unVisited)

    # 判断未访问的url队列是否为空
    def unVisitedUrlsEnmpy(self):
        return len(self.unVisited) == 0


def main(seeds,reurl):
    craw = MyCrawler(seeds)
    craw.crawling(reurl)

def get_seed():
    #获取种子URL 以及正则URL
    with open('/Users/administrator/PycharmProjects/untitled4/pachong/seed.txt')as f:
        txt = f.readlines()
    return txt[0],txt[1]




if __name__ == "__main__":
    a,b =get_seed()
    main(a,b)