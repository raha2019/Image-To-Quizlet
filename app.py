from flask import Flask, render_template, request
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "."
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/upload')
def upload_image():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
