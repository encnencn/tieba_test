# -*-encoding:utf-8 -*-
# ---------------------------------------
#   程序：南华大学贴吧获取器  
#   作者：ZZC  
#   日期：2017-03-21  
#   语言：Python 3.6
#   功能：爬取南华大学贴吧标题的内容。
# ---------------------------------------


import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # 检测状态
        print(r.encoding + "  " + r.apparent_encoding)
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return "getHTMLText"


def getTitleList(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    # 寻找符合条件的ul
    ul = soup.find_all('ul', attrs={'class': 'threadlist_bright j_threadlist_bright'})
    count = 0
    print("第一页")
    for i in ul:
        liTop = i.find_all('li', attrs={'class': ' j_thread_list thread_top j_thread_list clearfix'})
        print("有" + str(len(liTop)) + "个置顶帖")
        print("-------------------------------------")
        for j in liTop:
            count = count + 1
            getMessage(count, j, 0)
        liList = i.find_all('li', attrs={'class': ' j_thread_list clearfix'})
        print("-------------------------------------")
        print("有" + str(len(liList)) + "个普通帖")
        print("-------------------------------------")
        for j in liList:
            count = count + 1
            getMessage(count, j, 1)


def getMessage(count, j, top):
    huifu = j.find('span', attrs={'class': 'threadlist_rep_num center_text'})
    title = re.findall(r'<a .*?href="/p/\d{10}".*?>(.*?)</a>', str(j))
    author = j.find('span', attrs={'class': 'frs-author-name-wrap'})
    createTime = j.find('span', attrs={'class': 'pull-right is_show_create_time'})
    content = ""
    if top == 1:
        divCon = j.find('div', attrs={'class': 'threadlist_abs threadlist_abs_onlyline '})
        content = divCon.string.lstrip()
    print(count)
    if(title):
        print("标题:" + title[0])
    else:
        print("标题:" + "为空吧")

    try:
        print("作者:" + author.string)
    except TypeError:
        print("作者:" + "异常为空")

    if(createTime):
        print("时间：" + createTime.string)
    else:
     print("createTime:" + "为空")

    if(createTime):
        print("回复次数:" + huifu.string)
    else:
        print("huifu:" + "为空")

    if (content):
        print("内容：" + content)
    else:
        print("content:" + "为空")



def main():
    url = 'http://tieba.baidu.com/python'
    #url = 'http://tieba.baidu.com/p/4852364776?pid=120452934749&cid=120460022627#120460022627'
    getTitleList(url)


# -------- 程序入口处 ------------------
main()
