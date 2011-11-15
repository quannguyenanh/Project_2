from flask import Flask, redirect, request

app = Flask(__name__)

target_url = 'http://mydomain2.com/register.php?'
import re


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def redirect_url(path):
    return 'Input path: %s' % path
    if re.match(r"^([a-z0-9._-]+)(: [0-9]+)?",path) and request.method == 'GET':
        return redirect(target_url, 301)

if __name__ == '__main__':
    app.run()
