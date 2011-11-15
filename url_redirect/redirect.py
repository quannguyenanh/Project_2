from flask import Flask, redirect, request

app = Flask(__name__)
sub_url = 'abcd1234'
domain_url = 'domain1'
target_url = 'http://mydomain2.com/register.php?'
import re

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    #return 'You want path: %s' % path
    if re.match (sub_url, path) and re.match (domain, path) request.method == 'GET':
            return redirect(target_url, 301)
    
if __name__ == '__main__':
    app.run()
