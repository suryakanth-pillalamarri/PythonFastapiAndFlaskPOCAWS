from flask import Flask, render_template, request, send_file
from docxconverter import PDFTODOCX
import os

app = Flask(__name__)



#make it dynamic path ---comment 
UPLOAD_FOLDER = r'D:\Surya files\pythonaws_poc_2024\first_problem\inputfile'
DOWNLOAD_FOLDER = r"C:\Users\surya\Downloads"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        if 'pdf_file' not in request.files:
            raise Exception("No PDF file uploaded for conversion")

        pdf_file = request.files['pdf_file']
        if pdf_file.filename == '':
            raise Exception("Not  selected any file for conversion")

        # Save the uploaded PDF file
        pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
        pdf_file.save(pdf_file_path)

        # Convert PDF to DOCX
        converter = PDFTODOCX()
        docx_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], os.path.splitext(pdf_file.filename)[0] + ".docx")
        success, message = converter.convert(pdf_file_path, docx_file_path)

        if success:
            # Return the converted DOCX file for download
            return send_file(docx_file_path, as_attachment=True)
        else:
            raise Exception(message)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
