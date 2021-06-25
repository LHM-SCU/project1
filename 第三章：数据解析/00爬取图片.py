# 项目需求：爬取糗事百科指定页面的糗图，并将其保存到指定文件夹中
import requests
import json
import re
# re为使用正则表达式

if  __name__ == '__main__':
    url='https://book.apeland.cn/media/images/2019/04/15/snip20190415_24.png'
    # content返回的是二进制形式的图片数据
    # text(字符串) content（二进制） json()(对象)
    img_data=requests.get(url=url).content
    # Python3给open函数添加了名为encoding的新参数，而这个新参数的默认值却是‘utf-8’。
    # 这样在文件句柄上进行read和write操作时，系统就要求开发者必须传入包含Unicode字符的实例，而不接受包含二进制数据的bytes实例。
    # 使用二进制写入模式（‘wb’）来开启待操作文件，而不能像原来那样，采用字符写入模式（‘w’）
    with open('./lianhua.jpg', 'wb') as fp:
        fp.write(img_data)
    print('爬取数据结束')