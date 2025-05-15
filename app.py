from flask import Flask, render_template, request
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data_url = request.form['image']
    header, encoded = data_url.split(",", 1)
    binary_data = base64.b64decode(encoded)

    filepath = os.path.join(UPLOAD_FOLDER, 'captured_image.png')
    with open(filepath, "wb") as f:
        f.write(binary_data)

    return 'Image received and saved!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
