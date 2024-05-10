from flask import Flask, render_template,session,redirect
app = Flask(__name__)
app.secret_key = 'Tabakhna7@'
@app.route('/')
def count():
    
   if 'counter' not in session:
     session['counter']=0
   else:  
     session['counter']=  session['counter']+1
   
   return render_template("index.html" , counter=session['counter'])

@app.route('/destroy_session' , methods=['POST'])
def clear():
    session.clear()
    return redirect ('/')
@app.route('/two' , methods=['POST'])
def incrementtwo():
    if 'counter' not in session:
       session['counter']=0
    else:  
       session['counter']=  session['counter']+1
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)

    