from flask import Flask , render_template  # type: ignore
app = Flask(__name__)    
@app.route('/play')
def render_three_blue_boxes():
    return render_template('index.html', num_boxes=3, color='blue')
@app.route('/play/<int:x>')
def render_boxes(x):
    return render_template('index.html', num_boxes=x, color='blue')
@app.route('/play/<int:x>/<color>')
def render_colored_boxes(x, color):
    return render_template('index.html', num_boxes=x, color=color)


if __name__=="__main__":    
    app.run(debug=True)   
