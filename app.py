from flask import Flask, render_template,request
import random
import db



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topmenuback')
def topmenu_back():
    return render_template('index.html')

@app.route('/foodlist')
def food_list():
    food_list = db.select_all_foods()
    return render_template('food_list.html', food=food_list)

@app.route('/food_search', methods=['POST'])
def food_search():
    keyword= request.form.get('keyword')
    
    s_keyword=db.search_food(keyword)
    
    return render_template('search_result.html',food=s_keyword)

@app.route('/foodregisterinput')
def food_register_input():
    return render_template('food_register.html')

@app.route('/food_register', methods=['POST'])
def food_register():
 
    name= request.form.get('name')
    make= request.form.get('make')
    worth= request.form.get('worth')
    stock= request.form.get('stock')
    
    db.insert_food(name, make, worth, stock)
    
    return render_template('register_sucsess.html')

@app.route('/fooddeleteinput')
def food_delete_input():
    return render_template('food_delete.html')

@app.route('/food_delete', methods=['POST'])
def food_delete():
 
    id= request.form.get('id')
   
    
    db.delete_food(id)
    
    return render_template('delete_sucsess.html')

@app.route('/foodsearchinput')
def food_search_input():
    return render_template('food_search.html')



if __name__ == "__main__":
    app.run(debug=True)




