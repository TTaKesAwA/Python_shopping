from flask import Flask, render_template,request
import random
import db


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foodlist')
def food_list():
    food_list = db.select_all_foods()
    return render_template('food_list.html', food=food_list)

@app.route('/foodregisterinput')
def food_register_input():
    return render_template('food_register.html')

@app.route('/food_register', methods=['POST'])
def food_register():
 
    name= request.form.get('name')
    make= request.form.get('make')
    worth= request.form.get('worth')
    
    db.insert_food(name, make,worth)
    
    return render_template('register_sucsess.html')

if __name__ == "__main__":
    app.run(debug=True)




