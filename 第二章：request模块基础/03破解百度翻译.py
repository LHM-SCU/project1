# 爬取一整张页面中的局部数据
# 以百度翻译为例，只想拿到单词对应的翻译结果
# 页面中有局部刷新，涉及到ajxs,在抓包中看network 勾选xhr
import requests
import json
if  __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.UA伪装
    # post请求参数处理（同get请求一致）
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    # 3.post请求参数处理
    word = input('enter a word')
    data ={
        'kw':word
    }
    # data种封装携带的参数
    # 4。发送请求
    response = requests.post(url=post_url,data=data,headers=headers)
    # 5.获取响应数据:json()方法返回的是obj（如果确认响应数据是json格式的，才可以使用json（））
    # 在响应头headers中 respense headers中 content-type有 application/json
    dic_obj = response.json()
    print(dic_obj)

    # 进行持久化存储
    filename = word+'.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii = False)
    print('over')

