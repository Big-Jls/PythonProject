# 爬虫

## urllib
-- 理解请求头，请求参数，请求结果

-- 初步使用GET/POST方法。

-- request.urlopen()方法来获取相应数据。

-- request.Request创建相应对象，可以通过method设置类型，data、headers、以及url。 

-- headers请求头、parse.urlencode({})URL编码、parse.unquote()URL解码

1. **GET请求：**



```
    data = parse.urlencode({
        "name":"张三",
        "password":"<PASSWORD>"
    })
    url = f'http://httpbin.org/get?{data}'
    req = request.Request(url, headers=header, method = 'GET')
```


2. **POST请求：**


    
```
    data = parse.urlencode({
        "name":"张三",
        "password":"<PASSWORD>"
    }).encode()
    url = 'http://httpbin.org/post'
    req = request.Request(url, headers=header, method='POST', data=data)
```



## requests

1. **GET请求：**



```
    url = 'http://httpbin.org/get'
    res = requests.get(url)
    print(res.json())
    print('-------------------')
    res2 = requests.get(url)
    print(res2.text)
    print('-------------------')
    res2 = requests.get(url)
    print(res2.content.decode('utf-8'))
```


高级请求json()能让得到的json类型的HTTP对象直接转换成json对象输出，
中级请求text是转换成string字符串，
低级请求content得到的是未解码的字节流，当遇到text和json无法自动解析的时候可以用content进行手动解码。
例如：图片类的字节流，百度等。

2. **POST请求：**



```
    url = 'http://httpbin.org/post'
    response = requests.post(url,data={
        'name':'zs',
        'psw': 123456
    })
    print(response.json())
    
    url = 'http://httpbin.org/post'
    response2 = requests.post(url,json={'name':'zs',"pswd":"<PASSWORD>"})
    print(response2.json())
```


302重定向：
allow_redirects=False禁止重定向，默认是True

3. **Cookie：**



```
    url = 'https://vip.hdbz.net/auth/ajaxlogin'
    favorite_url = 'https://vip.hdbz.net/site/FavoriteList?page=1&limit=10'
    data = {
        "username": "******",
        "userpwd": "*******"
    }
    response = requests.post(url, data=data)
    res = requests.get(favorite_url,cookies=response.cookies)
    print(res.json())
```



4. **Session：**
session可以自动管理cookie，每次使用cookie的时候很不方便，session只用获取一次cookie之后再次
使用cookie就不用再次获取了，session帮你自动获取。


    
```
    url = 'https://vip.hdbz.net/auth/ajaxlogin'
    favorite_url = 'https://vip.hdbz.net/site/FavoriteList?page=1&limit=10'
    session = requests.Session()
    data = {
        "username": "*******",
        "userpwd": "*********"
    }
    res = session.request(url=url, data=data, method='post')
    print(res.cookies)
    res1 = session.request(url = favorite_url, method='get')
    print(res1.json())
```
## re
正则匹配

```
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>aTitle发发发1</title>
</head>
<body>
    <ul>
        <li id="item1">醒醒啦1</li>
        <li id="item2">醒醒啦2</li>
        <li id="item3">醒醒啦3</li>
        <li id="item4">醒醒啦4</li>
        <li id="item5">醒醒啦5</li>
    </ul>
    <p>
        hello
        i
        am
        iron
        man
    </p>"""
```    
1. **search：**

search找一个，n个括号就有n+1个group，可以用group(n)取值

```
    ul = re.search(r'<ul>(.*?)</ul>').group(1)
```

2. **findall：**

findall找多个，返回list列表

```
    lis = re.findall(r'<li id=".*?">(.*?)</li>')
    for li in lis:
        print(li)
```


## lxml
1. **etree：**
```
    from lxml import etree
    tree = etree.HTML(html)
    # Element html
    print(tree, dir(tree))
    print(tree.tag, tree.attrib['lang'], tree.text)
    
    # 一层一层的查找，类似面向对象的思想，过于麻烦。
    # 建议使用XPath
    head = tree.find("head")
    title = head.find("title")
    print(title.tag, title.text)
    
    body = tree.find("body")
    ul = body.find("ul")
    lis = ul.findall("li")
    
    for li in lis:
        print(li.text,  li.attrib["id"])
```
2. **XPath：**

xpath 语法

/ 根目录

// 任意目录 *

./ 当前目录

.// 当前目录下的任意目录 *

查找任意目录下存在id属性的li：
//li[@id]

查找任意目录下存在id属性为item5的li：
//li[@id=item5]

查找任意目录下alt属性包含 醒 的li：
//li[contains(@alt, "醒")]

查找任意目录下位置>1及第一个 li：
//li[position()>1]

查找任意目录下id是container的 li：
//*[@id="container"]

查找任意目录下id是item3 li的文本：
//li[@id="item3"]/text()

查找任意目录下id是item3 li的titles属性值：
//li[@id="item3"]/@title