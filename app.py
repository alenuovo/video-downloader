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
    
    # Absolute path to cookies file (adjust if needed)
    cookies_path = os.path.join(os.path.dirname(__file__), 'youtube_cookies.txt')
    
    try:
        subprocess.run(['yt-dlp', '--cookies', cookies_path, url], check=True)
        return 'Download started.'
    except subprocess.CalledProcessError as e:
        return f'Error downloading: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
