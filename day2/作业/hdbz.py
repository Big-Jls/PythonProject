import time
import requests
import re
url = 'https://www.hdbz.net/'
response = requests.get(url)
html = response.content.decode('utf-8')
m = re.search('<div class="clearfix pic-auto pic-list">(.*?)<div class="layout auto mt15">', html, re.S)
# print(m.group(1),type(m.group(1)))
m_group = m.group(1)
# 缩略图
m1 = re.findall('data-original="(.*?)"',m_group, re.S)
# print(m1)
# for img_thumbs_url in m1:
#     response = requests.get(img_thumbs_url)
#     match = re.search(r'/(\d+)\.(jpg|png)', img_thumbs_url)
#     if match:
#         img_id = match.group(1)
#         img_ext = match.group(2)
#         with open(f'./images/thumbs/{img_id}.{img_ext}', 'wb') as f:
#             f.write(response.content)
#         print(f"成功保存图片: {img_id}.{img_ext}")
#         time.sleep(0.5)

# 预览图
m2 = re.findall('href="(.*?)"',m_group, re.S)
for preview_part in m2:
    if not re.search(r'(collection?)',preview_part):
        preview_url = url + preview_part
        preview_url_response = requests.get(preview_url)
        preview_html = preview_url_response.content.decode('utf-8')
        # print(preview_html)
        preview_div = re.search('<div class="pic-preview">(.*?)</div>', preview_html, re.S).group(1)
        preview_image = re.search('src="(.*?)"',preview_div).group(1)
        preview_image_response = requests.get(preview_image)
        match = re.search(r'/(\d+)\.(jpg|png)', preview_image)
        if match:
            img_id = match.group(1)
            img_ext = match.group(2)
            # print(preview_image_response.content.decode('utf-8'))
            with open(f'./images/preview/{img_id}.{img_ext}', 'wb') as f:
                f.write(preview_image_response.content)
            print(f"成功保存图片: {img_id}.{img_ext}")
            time.sleep(0.5)
