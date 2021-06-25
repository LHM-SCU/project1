# 项目需求：爬取糗事百科指定页面的糗图，并将其保存到指定文件夹中
import requests
import json
import re
# re为使用正则表达式
import os
import time

if  __name__ == '__main__':
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # url中可以有不同的页面，设置一个通用的url模板
    url='https://www.qiushibaike.com/imgrank/page/%d/'
    # pageNum = 1
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    for pageNum in range(1,2):
        # 对应页码的url
        new_url = format(url%pageNum)  #适应格式化

        # 使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

        # 使用聚焦爬虫将页面中所有的图进行解析、提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

        # re.S是单行匹配 re.M是多行匹配
        img_src_list = re.findall(ex,page_text,re.S)

        # print(img_src_list)

        for src in img_src_list:
            # 拼接处一个完整的图片地址url
            src = 'http:'+src
            #请求到了图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片的名称,以‘/’切分，取倒数第一个值为图片的名称
            img_name = src.split('/')[-1]
            #图片存储的路径
            imgpath='./qiutuLibs/'+img_name
            with open(imgpath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功')



    # with open('./lianhua.jpg', 'w', encoding='utf-8') as fp:
    #     fp.write(img_data)
    # print('爬取数据结束')