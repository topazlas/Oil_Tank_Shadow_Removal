import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    if 'image' not in request.files:
        return render_template('index.html', ml_label="No Files")

    file = request.files['image']

    if file.filename == '':
        return render_template('index.html', ml_label="No Files")

    if file:
        # 파일 이름을 안전하게 처리하여 저장
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # 이미지를 저장한 경로
        pathname = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        subprocess.run(['python', 'final_main.py'])
        return render_template('predict.html', ml_label="Image uploaded successfully", print_image=filename)

@app.route('/delete_images')
def delete_images():
    folders = ['static/output', 'static/mask', 'static/uploads']
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    return 'Images deleted successfully!'


if __name__ == '__main__' :
  app.run(host='0.0.0.0', port=8000, debug=True)
