#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *

bot = Bot(cache_path=True)

# 定位公司群
#company_group = bot.groups().search('公司微信群')[0]

# 定位老板

#boss = company_group.search('老板大名')[0]
#boss = bot.search(u'A梓煜')[0]

# 将老板的消息转发到文件传输助手
bot.file_helper.send("王宝强")
# 堵塞线程
embed()