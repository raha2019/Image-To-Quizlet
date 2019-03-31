from flask import Flask, render_template, request
from tesseract import process_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "."
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/upload')
def upload_image():
    return render_template('upload.html')
def show():
    return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

    return render_template('test.html')
    return process_image(f.filename)


if __name__ == '__main__':
    #set debug to false if using in production environment
    app.run(debug = True, host='0.0.0.0')
