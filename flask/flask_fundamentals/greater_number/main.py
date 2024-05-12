from flask import Flask,render_template,session,request,redirect 
import random
app = Flask(__name__)   
app.secret_key='asasasasasas100'
@app.route('/')         
def index():
    if 'random' not in session:
        session['random']=random.randint(1,100)
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html') 

@app.route("/number", methods=['POST'])
def game():
    session['counter']+=1
    guessed_number=int(request.form['random number'])
    if guessed_number > session['random']:
        session['message'] = 'Too high!'
    elif guessed_number < session['random']:
        session['message'] = 'Too low!'
    elif guessed_number == session['random']:
        session['message']='Win'
    return redirect ('/')

@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":    
    app.run(debug=True)    

