from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    if not url:
        return 'No URL provided', 400

    # Generate unique filename
    filename = f"{uuid.uuid4()}.mp4"
    output_path = os.path.join("/tmp", filename)

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
        'cookies': 'cookies.txt',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"Error downloading: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
