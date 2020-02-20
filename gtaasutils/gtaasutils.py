import random


# 随机返回请求头
def getHeaders():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    ]

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    return headers


# 解析2天前、2分钟等这种日期格式
def format_datetime(dt):
    ret = ''
    if '分钟前' in dt:
        m = int(dt.split('分钟')[0])
        ret = (datetime.datetime.now() - datetime.timedelta(minutes=m)).strftime("%Y-%m-%d %H:%M:%S")
    elif '小时前' in dt:
        ms = int(dt.split('小时')[0]) * 60
        ret = (datetime.datetime.now() - datetime.timedelta(minutes=ms)).strftime("%Y-%m-%d %H:%M:%S")
    elif '秒前' in dt:
        secs = int(dt.split('秒')[0])
        ret = (datetime.datetime.now() - datetime.timedelta(seconds=secs)).strftime("%Y-%m-%d %H:%M:%S")
    elif '天前' in dt:
        d = int(dt.split('天')[0])
        ret = (datetime.datetime.now() - datetime.timedelta(days=d)).strftime("%Y-%m-%d %H:%M:%S")
    elif '昨天' in dt:
        ret = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    elif '前天' in dt:
        ret = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
    else:
        ret = dt
    return ret
