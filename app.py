from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Directory where files are stored
FILE_DIRECTORY = '.'

@app.route('/download/mp3/<filename>')
def download_mp3(filename):
    # Check if the file exists
    if not os.path.isfile(os.path.join(FILE_DIRECTORY, filename)):
        abort(404)
    return send_from_directory(directory=FILE_DIRECTORY, path=filename, as_attachment=True)

@app.route('/download/zip/<filename>')
def download_zip(filename):
    # Check if the file exists
    if not os.path.isfile(os.path.join(FILE_DIRECTORY, filename)):
        abort(404)
    return send_from_directory(directory=FILE_DIRECTORY, path=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
