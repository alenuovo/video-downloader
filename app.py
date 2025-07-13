from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    cookies_path = os.path.join(os.path.dirname(__file__), 'cookies.txt')

    if os.path.exists(cookies_path):
        command = ['yt-dlp', '--cookies', cookies_path, url]
    else:
        command = ['yt-dlp', url]

    subprocess.run(command)
    return 'Download started.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
