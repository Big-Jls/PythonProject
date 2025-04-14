import requests
import random
import hashlib

# 浏览器指纹
# url = 'https://tls.browserleaks.com/json'
# r = requests.get(url)
# print(r.text)

# 1.模拟请求去重 set()
# urls = [f'http://httpbin.org/get?name=张三&age={random.randint(1,100)}' for _ in range(1,101)]
# print(len(urls))
# fingerprint_set = set(urls)
# print(len(fingerprint_set))

# 2.利用hash去重
urls = [f'http://httpbin.org/get?name=张三&age={random.randint(1,100)}' for _ in range(1,101)]
print(len(urls))
pass_urls = []
fingerprint_set = set()
for url in urls:
    fingerprint = hashlib.md5(url.encode()).hexdigest()
    if fingerprint in fingerprint_set:
        pass
    else:
        fingerprint_set.add(fingerprint)
        pass_urls.append(url)
print(len(pass_urls))
