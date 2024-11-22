from flask import Flask
from flask import Flask, render_template, request
import flask
from PIL import Image
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload/', methods=['POST'])
def upload():
    if 'files[]' not in request.files:
        return 'Нет файлов, выбранных для загрузки.'
    files = request.files.getlist('files[]')
    images = []
    for file in files:
           if file and allowed_file(file.filename):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            images.append(file_path)
    if len(images) != 0:
        pdf_path = create_pdf(images)
        return flask.send_file(pdf_path, as_attachment=True)
    else:
        return "Неизвестный формат файла"


def create_pdf(images):
    ls = []
    for file in images:
        file = Image.open(file)
        file.save('output.pdf', save_all=True, append_images=[*ls])
        ls.append(file)
    file = 'output.pdf'
    return file
    os.rmdir('/uploads/')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['pdf', 'png', 'jpg', 'jpeg', 'gif']
    if filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False
   

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

