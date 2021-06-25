# bs4是python语言所特有的
import requests
from bs4 import BeautifulSoup
if  __name__ == '__main__':
    # 想要将本地的html文档中的数据加载到该对象中
    fp =open('./index.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup)

    # soup.tagName返回的是是html中第一次出现的tagname标签
    print(soup.a)
    print(soup.div)
    # soup.find('tagName'):等于soup.div
    #
    print(soup.find('div'))
    print(soup.find('div',class_= 'lines'))

