# TEST
Video clawer
抓取爱奇艺、腾讯视频、优酷视频上的相关信息
seed.txt第一行为起始url，第二行为需要匹配的正则。
起始文件zhuaqu.py采用广度优先，每个url页面里匹配正则的url加入队列继续抓，直到结束。
