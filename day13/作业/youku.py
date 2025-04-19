import json
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent(os='Windows')
url = 'https://www.youku.com/profile/index/?uid=UMTQ5NTM0ODcxNg=='
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://www.kdocs.cn/',
    'cookie':'isI18n=false; cna=5ffrH9jEBQ4CAXug4zwuw7kM; __ysuid=1734674916918lzg; HISTORY_KEY=%5B%22%E7%88%B1%E6%8B%8D%22%5D; P_gck=NA%7CRcIZQR4gOXLoVK1pCCtqFA%3D%3D%7CNA%7C1744169524779; P_pck_rm=pLJsmd1n9b027b9b49624cZB8gbmziRjGMY3gg%2FX5BR7cQt56t7KejYd6fUWPQSVzi6bZ9Owm6QC07ewvsVjqGs7YsfRYNiPfT9NVzZ1R8k8S5AWJwlUtY8wSS0ALOMu8XcoTt5bw6iyVRVOlqTfbcgAi4emlaHbWPhD4A%3D%3D%5FV2; disrd=63669; user_name=%E9%95%BF%E7%94%9F%E6%B7%B7%E6%B2%8C; 35638-index=1; 35638-startTime=1744170304313; isg=BAQE96mJPwJ3eYtexJfZYxpi1YL2HSiHZBhekR6lkU-SSaUTRiwVFoXgjeGR0WDf; csrfToken=ksKf4YPNr2QK683o6LDDHNIn; __ayft=1744872062836; __aysid=174487206283672L; __arpvid=1744872062836VsNDK5-1744872062848; __ayscnt=1; __aypstp=1; __ayspstp=1; _m_h5_tk=4299d10f4d885660e7546e290020a95a_1744877105448; _m_h5_tk_enc=5d9534ea0e7629c8242b3da3e26995c5; xlly_s=1; tfstk=gUEsIl2CzCAsECA3I1BEFZQAEfofLSsPGKMYE-KwHcn9MIe-TdlZQ5-YRSFn7fnquSTb_WUZ6PyqhnwitSgcIjlxGSyY79SP4R2immBPagSPbJYK9lGvgmnivWOpA2jP4R29QABzpgr4I4so1jnxWqHKpXD2MIFxWDIKtxDv6xKOdJhn9ALx6x3p9YD2XmnYMJBInXhxwX9ShNGgCOj2BigAiY2tOnKYXi0sNlY2DnEICVZYLXwaQkMs5b33XhGUXWyYbl0hRen0LzNbkSby-cwYWcHzIGtI2RUUcvrV3EGTLkwLxVpAwb3j1yEtRKKYpcljyrN11FcT7Wgop2pfqvPr9RqTRtALB7lsXv3F2TwKkyrirl5pf0UuQczYia8nf-UtAg-e4bwHDE9IrnMIa96BoEbzae2dkq2ATVHnC2WCdCUmWvDIa96BoE0tKAMPd9OTo'
}
response = requests.get(url, headers=headers)
# print(response.text)
html = response.text
nextSession_list = re.findall('nextSession":"(.*?)"componentId',html, re.S)[1].replace('\\','')[0:-4]
nextSession_list = json.loads(nextSession_list)
nextSession = {
    'nextSession': nextSession_list
}
print(nextSession)