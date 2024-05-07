from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruit_quantities = {
        "Strawberry": int(request.form.get('strawberry', 0)),
        "Raspberry": int(request.form.get('raspberry', 0)),
        "Apple": int(request.form.get('apple', 0))
    }
    customer_info = {
        "first_name": request.form.get('first_name', ''),
        "last_name": request.form.get('last_name', ''),
        "student_id": request.form.get('student_id', '')
    }
    total_fruits = sum(fruit_quantities.values())
    return render_template("checkout.html", fruits=fruit_quantities, customer=customer_info, total=total_fruits)

@app.route('/fruits')         
def fruits():
    fruits_list = [
        {"name": "Strawberry", "image": "strawberry.png"},
        {"name": "Raspberry", "image": "raspberry.png"},
        {"name": "Apple", "image": "apple.png"}
    ]
    return render_template("fruits.html", fruits=fruits_list)

if __name__=="__main__":   
    app.run(debug=True)    