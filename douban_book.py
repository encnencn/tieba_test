from bs4 import BeautifulSoup
import requests
import re
import codecs
from openpyxl import Workbook

excel_name = "书籍.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title = '书籍'


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    html = requests.get(url, headers=header).content
    return html


def get_con(html):
    soup = BeautifulSoup(html, 'html.parser')
    book_list = soup.find('div', attrs={'class': 'article'})
    page = soup.find('div', attrs={'class': 'paginator'})
    next_page = page.find('span', attrs={'class': 'next'}).find('a')
    name = []
    auther = []
    for i in book_list.find_all('table'):

        book_name = i.find('div', attrs={'class': 'pl2'})
        m = list(book_name.find('a').stripped_strings)

        book_auther = i.find('p', attrs={'class': 'pl'})
        u = list(book_auther.stripped_strings)

        if len(m) > 1:
            x = m[0] + m[1]

        else:
            x = m[0]

        if len(u) > 1:
            y = u[0] + u[1]

        else:
            y = u[0]
        print("x:"+x)
        print("y:"+y)
        name.append(x)
        auther.append(y)
    if next_page:
        return name, auther, next_page.get('href')
    else:
        return name, auther, None


def main():
    url = 'https://book.douban.com/top250'
    name_list = []
    auther_list = []
    while url:
        html = get_html(url)
        name, auther, url = get_con(html)
       #print(name_list.__len__())
        #print(auther_list.__len__())
        name_list = name_list + name
        auther_list = auther_list + auther
    for (i, m) in zip(name_list, auther_list):

        print("i:" + i)
        print("m:"+ m)
        col_A = 'A%s' % (name_list.index(i) + 1)
        col_B = 'B%s' % (name_list.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = m
    wb.save(filename=excel_name)


if __name__ == '__main__':
    main()
