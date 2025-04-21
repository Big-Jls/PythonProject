from DrissionPage import ChromiumPage

tab = ChromiumPage().latest_tab
tab.listen.start('www.douyin.com/aweme/v1/web/aweme/post')
tab.get('https://www.douyin.com/user/MS4wLjABAAAAtQDlEkazLfdG6escIuimqWap-F9a4Fr0_a2BtqzevM1hvf33gRIE8-PHIZR-u7Xx')

res = tab.listen.wait()
json_body = res.response.body
aweme_list = json_body['aweme_list']
print(len(aweme_list))