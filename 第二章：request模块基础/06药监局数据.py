import requests
import json
if __name__ == '__main__':
    # url = 'http://scxk.nmpa.gov.cn:81/xk/'
    # headers={
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    # }
    # page_text = requests.get(url=url,headers=headers).text

    # 这样请求到的页面中没有数据，说明数据不是靠地址栏中的url请求得到的，也不是靠ajax得到的
    # with open('./huazhuangpin.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    #     print('爬取数据结束')

    # 可以在ctrl+F 进行搜索对应的数据名称，发现网页代码中并没有想要的数据，即数据是动态记载出来的

    #获取url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    all_data_list=[]
    id_list=[] # 存储企业的id

    #参数的封装
    for page in range(1,6):
        page = str(page)
        data={
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, headers=headers,data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        print(id_list)

    # 获取企业的详情数据，拼接url
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data ={
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        print(detail_json)
        all_data_list.append(detail_json)
    # print('-----结束了 -----------')

    #持久化存储all_data_list
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('over')



