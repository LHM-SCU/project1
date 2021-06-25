# 在搜狗中录入一个关键字并检索
# 得到需要的结果

# UA检测：门户网炸的服务器回检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
# 则说明该请求是一个正常的请求，但是如果检测到请求的身份标识不是某一款浏览器，则表示该请求是不正常的
# User-agent（请求载体的身份标识）
# UA伪装：让爬虫对应的请求载体身份伪装为某一款浏览器
import  requests
if __name__ == "__main__":
    # 写明头信息,伪装成不同操作系统，不同浏览器的身份标识
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    # 处理url携带的参数:封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是含有参数，并且在请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    filename = kw+'.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
        print(filename,'保存成功')