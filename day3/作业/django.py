import requests
from lxml import etree

# json_api = 'http://localhost:8000/api/'
# response = requests.get(json_api)
# print(response.json())

# requests模拟登录
url = 'http://127.0.0.1:8000/admin/'
response = requests.get(url)
# print(response.text)
html = response.text
tree = etree.HTML(html)
# 获得对应的csrfmiddlewaretoken以便对login_url发送请求发送
csrfmiddlewaretoken = tree.xpath('//*[@id="login-form"]/input/@value')[0]
login_url = 'http://127.0.0.1:8000/admin/login/?next=/admin/'
data = {
    'csrfmiddlewaretoken': csrfmiddlewaretoken,
    'username': 'admin',
    'password': 'admin',
    'next': '/admin/'
}
cookies = {
    # 'Pycharm-ee4d39d0': '5dc92a8d-8551-4e63-8e2a-223192fb196d',
    'csrftoken': csrfmiddlewaretoken
}
# 发送post请求，携带data和cookies并且禁止重定向获取响应的cookies
login_response = requests.post(login_url, data=data, allow_redirects=False, cookies=cookies)

print(login_response.cookies)
# admin_url = 'http://localhost:8000/admin/'
# print(login_response.cookies.values())
# 响应的cookies包含csrftoken和sessionid
# 需要再次对url发送get请求，携带我们模拟登录后获得cookies
admin_login_response = requests.get(url, cookies=login_response.cookies)
# 显示登陆后的页面，模拟登录成功！
print(admin_login_response.text)
"""
<!DOCTYPE html>

<html lang="zh-hans" dir="ltr">
<head>
<title>站点管理 | Django 站点管理员</title>
<link rel="stylesheet" href="/static/admin/css/base.css">

  <link rel="stylesheet" href="/static/admin/css/dark_mode.css">
  <script src="/static/admin/js/theme.js"></script>


  <link rel="stylesheet" href="/static/admin/css/nav_sidebar.css">
  <script src="/static/admin/js/nav_sidebar.js" defer></script>

<link rel="stylesheet" href="/static/admin/css/dashboard.css">



    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/admin/css/responsive.css">
    

<meta name="robots" content="NONE,NOARCHIVE">
</head>

<body class=" dashboard"
  data-admin-utc-offset="0">
<a href="#content-start" class="skip-to-content-link">跳到主要内容</a>
<!-- Container -->
<div id="container">

    
    <!-- Header -->
    
      <header id="header">
        <div id="branding">
        
<div id="site-name"><a href="/admin/">Django 管理</a></div>


        </div>
        
        
        <div id="user-tools">
            
                欢迎，
                <strong>admin</strong>.
            
            
                
                    <a href="/">查看站点</a> /
                
                
                    
                    
                
                
                <a href="/admin/password_change/">修改密码</a> /
                
                <form id="logout-form" method="post" action="/admin/logout/">
                    <input type="hidden" name="csrfmiddlewaretoken" value="1KAjJtaISxO0jInx6JTj0a3xRCFCuQw5lSIU2315RSZIM1JL1rd6R0dwvDEwmAUo">
                    <button type="submit">注销</button>
                </form>
                
<button class="theme-toggle">
  <span class="visually-hidden theme-label-when-auto">切换主题（当前主题：自动）</span>
  <span class="visually-hidden theme-label-when-light">切换主题（当前主题：浅色）</span>
  <span class="visually-hidden theme-label-when-dark">切换主题（当前主题：深色）</span>
  <svg aria-hidden="true" class="theme-icon-when-auto">
    <use xlink:href="#icon-auto" />
  </svg>
  <svg aria-hidden="true" class="theme-icon-when-dark">
    <use xlink:href="#icon-moon" />
  </svg>
  <svg aria-hidden="true" class="theme-icon-when-light">
    <use xlink:href="#icon-sun" />
  </svg>
</button>

            
        </div>
        
        
        
      </header>
    
    <!-- END Header -->
    
    

    <div class="main" id="main">
      
        
      
      <main id="content-start" class="content" tabindex="-1">
        
          
        
        <!-- Content -->
        <div id="content" class="colMS">
          
          <h1>站点管理</h1>
          
          
<div id="content-main">
  


  
    <div class="app-index module">
      <table>
        <caption>
          <a href="/admin/index/" class="section" title="在应用程序 Index 中的模型">Index</a>
        </caption>
        
          
            <tr class="model-actor">
              <th scope="row" id="index-actor">
                
                  <a href="/admin/index/actor/">Actors</a>
                
              </th>

              
                <td><a href="/admin/index/actor/add/" class="addlink" aria-describedby="index-actor">增加</a></td>
              

              
                
                  <td><a href="/admin/index/actor/" class="changelink" aria-describedby="index-actor">修改</a></td>
                
              
            </tr>
          
        
          
            <tr class="model-category">
              <th scope="row" id="index-category">
                
                  <a href="/admin/index/category/">Categorys</a>
                
              </th>

              
                <td><a href="/admin/index/category/add/" class="addlink" aria-describedby="index-category">增加</a></td>
              

              
                
                  <td><a href="/admin/index/category/" class="changelink" aria-describedby="index-category">修改</a></td>
                
              
            </tr>
          
        
          
            <tr class="model-content">
              <th scope="row" id="index-content">
                
                  <a href="/admin/index/content/">Contents</a>
                
              </th>

              
                <td><a href="/admin/index/content/add/" class="addlink" aria-describedby="index-content">增加</a></td>
              

              
                
                  <td><a href="/admin/index/content/" class="changelink" aria-describedby="index-content">修改</a></td>
                
              
            </tr>
          
        
          
            <tr class="model-movies">
              <th scope="row" id="index-movies">
                
                  <a href="/admin/index/movies/">Moviess</a>
                
              </th>

              
                <td><a href="/admin/index/movies/add/" class="addlink" aria-describedby="index-movies">增加</a></td>
              

              
                
                  <td><a href="/admin/index/movies/" class="changelink" aria-describedby="index-movies">修改</a></td>
                
              
            </tr>
          
        
          
            <tr class="model-normaluser">
              <th scope="row" id="index-normaluser">
                
                  <a href="/admin/index/normaluser/">用户</a>
                
              </th>

              
                <td><a href="/admin/index/normaluser/add/" class="addlink" aria-describedby="index-normaluser">增加</a></td>
              

              
                
                  <td><a href="/admin/index/normaluser/" class="changelink" aria-describedby="index-normaluser">修改</a></td>
                
              
            </tr>
          
        
      </table>
    </div>
  
    <div class="app-auth module">
      <table>
        <caption>
          <a href="/admin/auth/" class="section" title="在应用程序 认证和授权 中的模型">认证和授权</a>
        </caption>
        
          
            <tr class="model-group">
              <th scope="row" id="auth-group">
                
                  <a href="/admin/auth/group/">组</a>
                
              </th>

              
                <td><a href="/admin/auth/group/add/" class="addlink" aria-describedby="auth-group">增加</a></td>
              

              
                
                  <td><a href="/admin/auth/group/" class="changelink" aria-describedby="auth-group">修改</a></td>
                
              
            </tr>
          
        
      </table>
    </div>
  


</div>

          
<div id="content-related">
    <div class="module" id="recent-actions-module">
        <h2>最近动作</h2>
        <h3>我的动作</h3>
            
            
            
            <ul class="actionlist">
            
            <li class="changelink">
                <span class="visually-hidden">已修改：</span>
                
                    <a href="/admin/index/normaluser/5/change/">user</a>
                
                <br>
                
                    <span class="mini quiet">用户</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/movies/28/change/">异形</a>
                
                <br>
                
                    <span class="mini quiet">Movies</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/69/change/">西格妮·韦弗</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/68/change/">雷德利·斯科特</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/movies/27/change/">电锯惊魂</a>
                
                <br>
                
                    <span class="mini quiet">Movies</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/67/change/">雷·沃纳尔</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/66/change/">温子仁</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/movies/26/change/">惊魂记</a>
                
                <br>
                
                    <span class="mini quiet">Movies</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/65/change/">安东尼·博金斯</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            <li class="addlink">
                <span class="visually-hidden">已添加：</span>
                
                    <a href="/admin/index/actor/64/change/">阿尔弗雷德·希区柯</a>
                
                <br>
                
                    <span class="mini quiet">Actor</span>
                
            </li>
            
            </ul>
            
    </div>
</div>

          <br class="clear">
        </div>
        <!-- END Content -->
      </main>
    </div>
    <footer id="footer"></footer>
</div>
<!-- END Container -->

<!-- SVGs -->
<svg xmlns="http://www.w3.org/2000/svg" class="base-svgs">
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-auto"><path d="M0 0h24v24H0z" fill="currentColor"/><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2V4a8 8 0 1 0 0 16z"/></symbol>
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-moon"><path d="M0 0h24v24H0z" fill="currentColor"/><path d="M10 7a7 7 0 0 0 12 4.9v.1c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2h.1A6.979 6.979 0 0 0 10 7zm-6 5a8 8 0 0 0 15.062 3.762A9 9 0 0 1 8.238 4.938 7.999 7.999 0 0 0 4 12z"/></symbol>
  <symbol viewBox="0 0 24 24" width="1rem" height="1rem" id="icon-sun"><path d="M0 0h24v24H0z" fill="currentColor"/><path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.415-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"/></symbol>
</svg>
<!-- END SVGs -->
</body>
</html>
"""