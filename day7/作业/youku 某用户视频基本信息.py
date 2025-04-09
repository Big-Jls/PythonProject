import time

import requests

headers = {
    # 'referer': 'https://www.youku.com/profile/index/?spm=a2hkm.8166622.PhoneSokuUgc_2.duploader&uid=UMTQ5NTM0ODcxNg==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    # 'cookie': 'isI18n=false; cna=5ffrH9jEBQ4CAXug4zwuw7kM; __ysuid=1734674916918lzg; csrfToken=9zcX8GRJ-9g45v4L67Dsi3jX; __ayft=1744166138740; __aysid=1744166138740jUr; __ayscnt=1; _m_h5_tk=4e57c0c97480a45caa6cc6872fc138d6_1744169739890; _m_h5_tk_enc=d2b786e90ca612e3004ef4d3f31ada40; xlly_s=1; 35654-index=1; 35654-startTime=1744166140234; __ayvstp=3; __aysvstp=3; HISTORY_KEY=%5B%22%E7%88%B1%E6%8B%8D%22%5D; login_index=2_1744166140233; isg=BExMGeALR2p_ElMGXP-RuxJ6Hap-hfAvfHDmqaYNWPeaMe07zpQJvoqI1TkJeSiH; __arpvid=1744166480720o2Odaa-1744166480750; __aypstp=5; __ayspstp=5; tfstk=gIUod7bQUuo7mbw9e-u5j0upwDIYiQgIQJLKp2HF0xkXeLL8Twy368t-YTg8--VQ9YEL2JL3n8eYJuLKzQZbB588yggp-4gI8OBOWNn7N2gEdL9eOYN4GX5xaWetpPgI8OBvDeo5S2w6Dt6LUS5m9Xpy8Joeuqli3X-r8Jkq0fl9U2uULsmq_b8yzYlzgKli3vuE8JPViXhyzekg8raVh24r-oZCboGoqAPrU7F8ugnWV7kD8ez0m4kwexYe8rcuMyVHyFjKQlM-XA2VkU03gX2-HR7woqogfWh3EaYryorbP4UAIpnuKxn3z7Xl-S4nEczrmBYLs4cULDqfIFhoyomgru1B37ytElu79CX8icqmfjo2t3u8X5UIbz7kCxnst8HYQN8muDSr-n-w2w8Ig6U2AHirGjDtO8hGiffVp81cihsS4jGRBsfDAHirGjDOisx6d0ljwOC..'
}

# nextSession = {"subIndex": 48, "trackInfo": {"parentdrawerid": "4433"}, "spmA": "miniapp", "level": 1,
#                "spmC": "drawer2", "spmB": "homepage", "index": 2, "pageName": "page_miniapp",
#                "scene": "home_page_component_paging", "scmB": "rcmd", "path": "EP573331", "scmA": "20140689",
#                "scmC": "24776", "tab": "", "id": 24776}
# print()
# 1744168524.9378674
# 1744166742629
# params = {
#     'type': 'video',
#     'pageNo': 2,
#     'nextSession': nextSession,
#     'uid': 'UMTQ5NTM0ODcxNg==',
#     'isGray': 0,
#     'extend': {},
#     '_': int(time.time() * 10),
#     'callback': 'axiosJsonpCallback2'
# }
#
# url = 'https://www.youku.com/profile/profile-data'
# response = requests.get(url, params=params, headers=headers)
# print(response.text)

# {"message":"success","data":{"componentList":[{"componentId":"pc-profile-video","componentName":"短视频","type":"video","moduleList":[],"logInfo":{"spmC":"tab","spmD":"videotab","spmAB":"miniapp.homepage","spm":"miniapp.homepage.tab.videotab","scm":"20140689.rcmd.tab.other_other","trackInfo":"{"servertime":1744167765363,"pagestate":1,"bizKey":"PGC_H5","cms_req_id":"21365f0517441677653537090e89a7"}"}},{"componentId":"pc-profile-dynamic","componentName":"动态","type":"dynamic","moduleList":[],"logInfo":{"spmC":"tab","spmD":"hometab","spmAB":"miniapp.homepage","spm":"miniapp.homepage.tab.hometab","scm":"20140689.rcmd.tab.other_other","trackInfo":"{"servertime":1744167765363,"pagestate":1,"bizKey":"PGC_H5","cms_req_id":"21365f0517441677653537090e89a7"}"}}],"pageData":{"shareInfo":{"title":"","link":"https://m.youku.com/profile?uid=UMTQ5NTM0ODcxNg==&callApp=1&callVideo=true","img":null,"describe":"快来看TA的精彩视频吧"},"spmA":"miniapp","spmB":"homepage","spmAB":"miniapp.homepage"}}}
# {"message":"success","data":{"componentList":[{"componentId":"pc-profile-video","componentName":"短视频","type":"video","moduleList":[],"logInfo":{"spmC":"tab","spmD":"videotab","spmAB":"miniapp.homepage","spm":"miniapp.homepage.tab.videotab","scm":"20140689.rcmd.tab.other_other","trackInfo":"{"servertime":1744167761816,"pagestate":1,"bizKey":"PGC","cms_req_id":"2104659117441677618068933e3e9d"}"}},{"componentId":"pc-profile-dynamic","componentName":"动态","type":"dynamic","moduleList":[],"logInfo":{"spmC":"tab","spmD":"hometab","spmAB":"miniapp.homepage","spm":"miniapp.homepage.tab.hometab","scm":"20140689.rcmd.tab.other_other","trackInfo":"{"servertime":1744167761816,"pagestate":1,"bizKey":"PGC","cms_req_id":"2104659117441677618068933e3e9d"}"}}],"pageData":{"shareInfo":{"title":"","link":"https://m.youku.com/profile?uid=UMTQ5NTM0ODcxNg==&callApp=1&callVideo=true","img":null,"describe":"快来看TA的精彩视频吧"},"spmA":"miniapp","spmB":"homepage","spmAB":"miniapp.homepage"}}}

# url = 'http://api.youku.com/api_ptvideo/st_5'
# params = {
#     'pid': 'UMTQ5NTM0ODcxNg==',
#     'sv': '%e7%88%b1%e6%8b%8d%e5%8e%9f%e5%88%9b_%e5%8e%9f%e6%9d%a5%e7%9a%84%e8%a7%86%e9%a2%91',
#     'rt': 3,
#     'pg': 1,
#     'pz': 100,
#     'ob': 1,
#     'owner': 'my'
# }
# response = requests.get(url, headers=headers, params=params)
# print(response.text)
