import time

from DrissionPage import ChromiumPage

tab = ChromiumPage().latest_tab
tab.listen.start('h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/?')
tab.get('https://zc-paimai.taobao.com/wow/pm/default/pc/4b80fa?page=2')
# time.sleep(5)
res = tab.listen.wait()
print(res.response.body)