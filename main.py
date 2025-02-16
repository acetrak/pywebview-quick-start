import webview
from flask import Flask,render_template

static_folder = 'gui/static'
template_folder = 'gui'

class Api:

    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def handle_url(self, url):
        print(url)


        response = {
            'status': 'ok',
            'html': 'div'
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

server = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

@server.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    api = Api()
    # window = webview.create_window('pywebview', 'http://localhost:5173', js_api=api, )
    window = webview.create_window('pywebview', server, js_api=api, )
    webview.start(debug=True)