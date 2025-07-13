from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    subprocess.run(['yt-dlp', '--cookies', 'www.youtube.com_cookies.txt', url])
    return 'Download started.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
