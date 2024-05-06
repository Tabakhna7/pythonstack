from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "put any number after the slash please for example /4  "

@app.route('/<int:x>')
def checkerboard_rows(x):
    return render_template('index.html', rows=x, cols=x, color1='blue', color2='red')

@app.route('/<int:x>/<int:y>')
def checkerboard_rows_columns(x, y):
    return render_template('index.html', rows=x, cols=y, color1='blue', color2='red')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_rows_columns_colors(x, y, color1, color2):
    return render_template('index.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)