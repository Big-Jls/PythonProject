# 爬虫

## urllib
-- 理解请求头，请求参数，请求结果

-- 初步使用GET/POST方法。

-- request.urlopen()方法来获取相应数据。

-- request.Request创建相应对象，可以通过method设置类型，data、headers、以及url。 

-- headers请求头、parse.urlencode({})URL编码、parse.unquote()URL解码

1. **GET请求：**


    data = parse.urlencode({
        "name":"张三",
        "password":"<PASSWORD>"
    })
    url = f'http://httpbin.org/get?{data}'
    req = request.Request(url, headers=header, method = 'GET')

2. **POST请求：**


    data = parse.urlencode({
        "name":"张三",
        "password":"<PASSWORD>"
    }).encode()
    url = 'http://httpbin.org/post'
    req = request.Request(url, headers=header, method='POST', data=data)


## requests

1. **GET请求：**


    url = 'http://httpbin.org/get'
    res = requests.get(url)
    print(res.json())
    print('-------------------')
    res2 = requests.get(url)
    print(res2.text)
    print('-------------------')
    res2 = requests.get(url)
    print(res2.content.decode('utf-8'))

高级请求json()能让得到的json类型的HTTP对象直接转换成json对象输出，
中级请求text是转换成string字符串，
低级请求content得到的是未解码的字节流，当遇到text和json无法自动解析的时候可以用content进行手动解码。
例如：图片类的字节流，百度等。

2. **POST请求：**


    url = 'http://httpbin.org/post'
    response = requests.post(url,data={
        'name':'zs',
        'psw': 123456
    })
    print(response.json())
    
    url = 'http://httpbin.org/post'
    response2 = requests.post(url,json={'name':'zs',"pswd":"<PASSWORD>"})
    print(response2.json())