import bs4
import requests
import os
import random
import argparse
import time

# 如提示未找到模块
# 请安装相应模块
# 例如： pip install bs4

agents = [
    # 谷歌
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.124 Safari/537.36',
    # 微软
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64',
    # 火狐
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
]

headers = {}

wrap_html = '''
           <html lang="zh">
               <head>
                 <meta charset="UTF-8">
                 <meta
                     name="viewport"
                     content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
                 >
                 <meta http-equiv="X-UA-Compatible" content="ie=edge">
                 <title>Document</title>
                 <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.25.0/prism.min.js"
                       integrity="sha512-hpZ5pDCF2bRCweL5WoA0/N1elet1KYL5mx3LP555Eg/0ZguaHawxNvEjF6O3rufAChs16HVNhEc6blF/rZoowQ=="
                       crossorigin="anonymous" referrerpolicy="no-referrer"></script>
                   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism-themes/1.9.0/prism-vs.min.css"
                       integrity="sha512-Jn4HzkCnzA7Bc+lbSQHAMeen0EhSTy71o9yJbXZtQx9VvozKVBV/2zfR3VyuDFIxGvHgbOMMNvb80l+jxFBC1Q=="
                       crossorigin="anonymous" referrerpolicy="no-referrer" />
                   <style>
                       html,
                       body {
                           background-color: #f5f5f5;
                           min-height: 100vh;
                       }

                       div {
                           box-sizing: border-box;
                       }

                       pre {
                         background-color: #f5f5f5;
                         padding: 10px;
                         border-radius: 8px;
                       }

                       .main {
                           max-width: 1200px;
                           margin: 30px auto;
                           background-color: #fff;
                           padding: 30px;
                           border-radius: 12px;
                       }

                       .article-info-box {
                           display: none;
                       }

                       #blogColumnPayAdvert {
                           display: none;
                       }

                       #blogExtensionBox{
                           display: none;
                       }
                   </style>
               </head>
               <body>
                   <div class="main">
                       <div>
                            <h6 style="color:red; font-size:18px;margin:20px 0 0px">免责声明：</h6>
                            <p>该脚本仅用于学习交流，请于24小时内删除，如你使用该脚本造成的后果一律由你本人承担</p>
                       </div>
                   </div>
               </body>
           </html>
       '''


def update_agent():
    r = random.randint(0, len(agents) - 1)
    headers.update({'User-Agent': agents[r]})


def get_headers():
    update_agent()
    return headers


def csdn(url, dir_name='csdn'):
    # create parser
    desc_str = "请输入参数."
    parser = argparse.ArgumentParser(description=desc_str)

    parser.add_argument('--url', dest='url', required=False)
    parser.add_argument('--dir_name', dest='dir_name', required=False)

    args = parser.parse_args()

    if args.url:
        url = args.url

    if args.dir_name:
        dir_name = args.dir_name

    if not url:
        print('请输入URl参数')
        return

    res = requests.get(url, headers=get_headers())

    html = bs4.BeautifulSoup(res.text, 'html.parser')

    title = html.find('h1').text.replace(" ", "")
    content = html.find('div', class_='blog-content-box')
    source_link = html.find('div', class_='article-source-link')

    [s.extract() for s in content(['script', 'link', 'img'])]  # 去除特定标签

    new_html = bs4.BeautifulSoup(wrap_html, 'html.parser')

    new_html.find('div', class_='main').insert(0, content)
    new_html.find('div', class_='main').insert(3, source_link)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    timestamp = int(time.time())
    date = time.strftime('%Y-%m-%d', time.localtime(timestamp))

    with open(f'{dir_name}/【{date}】{title}.html', 'w', encoding='utf-8') as f:
        f.write(str(new_html))

    return str(new_html)

# if __name__ == '__main__':
#     main('https://blog.csdn.net/qq_38612882/article/details/122323194')
