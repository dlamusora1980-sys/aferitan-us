from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для скачивания файла
@app.route('/download')
def download_file():
    # Файл должен лежать в папке static
    return send_from_directory('static', 'Aferitan Setup.exe', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
