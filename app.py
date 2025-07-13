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
    result = subprocess.run(
        ['yt-dlp', '--cookies', 'www.youtube.com_cookies.txt', '-o', 'downloads/%(title)s.%(ext)s', url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    return f"<pre>{result.stdout}</pre>"

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(host='0.0.0.0', port=5000)
