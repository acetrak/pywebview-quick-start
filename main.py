import webview
from script.csdn import csdn
from flask import Flask
from views import index_page

static_folder = 'gui/static'


class Api:

    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def handle_url(self, url):
        print(url)

        html = csdn(url)
        response = {
            'status': 'ok',
            'html': html
        }
        return response


def evaluate_js(window):
    result = window.evaluate_js(
        r"""
        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """
    )

    # print(result)


app = Flask(__name__, static_folder=static_folder)

app.register_blueprint(index_page, )

if __name__ == '__main__':
    api = Api()

    # window = webview.create_window('API example', 'http://127.0.0.1:5173', js_api=api, )
    window = webview.create_window('pywebview + vue3', app, js_api=api, )
    webview.start(debug=False)
