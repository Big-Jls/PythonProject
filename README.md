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
