import requests

url = 'https://www.bizhihui.com/page/'

for i in range(1,11):
    r_url = url + f'{i}/'
    r = requests.get(r_url)
    print(r.content.decode('utf-8'))
    break