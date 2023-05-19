
## pywebview  + vite + vue3 开发桌面应用

# 目录结构

-app  vite应用（前端）

-script  python脚本

-main.py  应用入口文件

# 开发阶段

1. 进入/app

`pnpm i`

`pnpm run dev`

2. 设置`main.py`中

```python

if __name__ == '__main__':
    api = Api()

    window = webview.create_window('API example', 'http://127.0.0.1:5173', js_api=api, )
    # window = webview.create_window('pywebview + vue3', app, js_api=api, )
    webview.start(debug=True)

```

3. 启动主程序

# 打包应用
1. 进入/app

`pnpm run build`


2. 设置`main.py`中


```python
if __name__ == '__main__':
    api = Api()

    # window = webview.create_window('API example', 'http://127.0.0.1:5173', js_api=api, )
    window = webview.create_window('pywebview + vue3', app, js_api=api, )
    webview.start(debug=False)

```

3.使用`auto-py-to-exe`打包

```bash
pip install auto-py-to-exe
# 启动工具
auto-py-to-exe
```

需要注意的是要在附加文件一块设置中将flask涉及到的模板, 静态文件, 还有其他诸如sqlite数据库文件都添加进去






 
参考 ：
1. https://zhuanlan.zhihu.com/p/101544546
2. https://juejin.cn/post/7113107801785761799