import requests
import json

if __name__ == '__main__':
    # 获取url 与 参数
    url='https://movie.douban.com/j/chart/top_list?'
    param ={
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',
        # 从库中的第几部电影去取
        'limit': '20'
        # 一次取出的个数
    }
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()

    # 持久化存储
    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over')

    # 在线json校验格式化工具
    # www.bejson.com
