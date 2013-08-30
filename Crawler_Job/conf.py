# -*- coding: utf-8 -*-
#设置你感兴趣的招聘信息关键词
TITLE_INCLUDE_KEYWORD = ['VMWare','360','Google','IBM','Microsoft','Intel','Adobe',u'百度',u'微软',u'移动',u'电信',u'银行',u'工商',u'建设',u'农业',u'华为',u'网易',u'腾讯',u'阿里',u'淘宝',u'豌豆夹',u'联想',u'完美',u'广移',u'航天',u'搜狗',u'搜狐',u'优酷',u'三星'] 

#设置你需要过滤掉的招聘信息关键词
TITLE_LIMIT_KEYWORD = ['被取消']

#设置招聘信息源 BYR(邮人论坛) NS_XZ(水木清华校招) NS_SZ(水木清华社招) NS_LT(水木清华猎头)
JOB_SOURCES = ['BYR_XZ','BYR_SZ','BYR_SX','NS_XZ','NS_SZ','NS_LT'] 

#设置每一个Tab显示不感兴趣招聘数目
SHOW_NUMBER = 30

#设置爬取招聘信息的间隔时间 #单位/小时
INTERVAL_TIME_CRAWLER = 0.2

SERVER_IP = '192.168.205.70'

SERVER_PORT = 8123
