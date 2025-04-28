import requests
from fake_useragent import UserAgent
def get_captcha(headers):
    url = 'https://passport.bilibili.com/x/passport-login/captcha?source=main_web'
    response = session.get(url,headers=headers)
    print(response.json())
    data = response.json()['data']
    token = data['token']
    geetest = data['geetest']
    gt = geetest['gt']
    challenge = geetest['challenge']
    return token, gt, challenge

def get_validate(headers, gt, challenge):
    url = f'https://api.geetest.com/ajax.php?gt={gt}&challenge={challenge}'
    response = session.get(url, headers=headers)
    print(response.text)
# # 1.人机验证步骤
# validate = 填写验证码(gt, challenge) # 这一步填写验证码 (访问极验API，得到validate)
#
# # 2.密码加密步骤
# pubkey, salt = 获取公钥和盐()
# 加密后的密码 = RSA公钥加密(pubkey, salt+password) # 盐需要加在密码字符串前
# base64编码后的密文 = base64编码(加密后的密码)
#
# # 3.开始登录
# cookie = 密码登录(username, base64编码后的密文, token, challenge, validate)
# 存储cookie(cookie)
# SSO登录页面跳转()

if __name__ == '__main__':
    username = '2333333'
    password = 'password'
    ua = UserAgent(os='Windows')
    headers = {
        'User-Agent': ua.random,
        'referer': 'https://www.bilibili.com/'
    }
    session = requests.session()
    token, gt, challenge = get_captcha(headers=headers)
    get_validate(headers, gt, challenge)
