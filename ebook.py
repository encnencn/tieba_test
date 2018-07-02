from bs4 import BeautifulSoup
import requests
import codecs
def get_url_list(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')#content如果换成text会有乱码
    url_list = []
    list = soup.select("#list > dl > dd > a")
    for i in list:
        i = i.get("href")
        i = 'http://www.biqugecom.com' + i
        url_list.append(i)
    url_list = url_list[9:-1]
    print (url_list)
    return url_list
def get_data(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    fo = codecs.open('output.txt', 'a+', 'utf-8');
    # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
    #Python学习群125240963
    section_name = soup.select("#wrapper > div.content_read > div > div.bookname > h1")[0].text
    print (section_name)
    fo.write(('\r\n' + section_name + '\r\n'))
    section_text = soup.select("#content")
    for x in section_text:
        a = x.text.replace('readx();', '').replace('www.biqugecom.com/20/20341/', '')
        fo.write((a)+ '\r\n')
    # 以二进制写入章节内容
    fo.close()  # 关闭小说文件
if '__main__' == __name__:
    url = 'http://www.biqugecom.com/27/27204/'#/34/34055/
    url_list = get_url_list(url)
    for n in url_list:
        get_data (n)