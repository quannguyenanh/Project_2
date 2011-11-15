from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_url():
    if request.method == 'GET':
        return redirect('http://127.0.0.1:8080', 301)
    
if __name__ == '__main__':
    app.run()
