from flask import Flask, render_template, request, redirect ,url_for, session
import db, string, random
from datetime import timedelta




app = Flask(__name__)
app.secret_key =''.join(random.choices(string.ascii_letters,k=256))




@app.route('/adminkari')
def admin_kari():
    return render_template('admin_topmenu.html')

@app.route('/adminlogin')
def admin_login():
    return render_template('adminlogin.html')

@app.route('/admintopmenuback')
def admin_topmenu_back():
    return render_template('admin_topmenu.html')

@app.route('/mypageback')
def mypageback():
    return render_template('mypage.html')

@app.route('/foodlist')
def food_list():
    food_list = db.select_all_foods()
    return render_template('food_list.html', food=food_list)

@app.route('/userfoodlist')
def user_food_list():
    food_list = db.select_all_foods()
    return render_template('user_food_list.html', food=food_list)

@app.route('/foodeditinput')
def food_edit_input():
    return render_template('food_edit_input.html')

@app.route('/foodedit', methods=['POST'])
def food_edit():
    id= request.form.get('id')
    name= request.form.get('name')
    make= request.form.get('make')
    worth= request.form.get('worth')
    stock= request.form.get('stock')
    db.edit_food(id,name, make, worth, stock)
    
    return render_template('editsucsess.html')

@app.route('/foodbuy', methods=['POST'])
def food_buy():
    id= request.form.get('id')
    
    db.food_buy(id)
    
    return render_template('buysucsess.html')

@app.route('/food_search', methods=['POST'])
def food_search():
    keyword= request.form.get('keyword')
    
    s_keyword=db.search_food(keyword)
    
    return render_template('search_result.html',food=s_keyword)


@app.route('/user_food_search', methods=['POST'])
def user_food_search():
    keyword= request.form.get('keyword')
    
    s_keyword=db.search_food(keyword)
    
    return render_template('usearch_result.html',food=s_keyword)

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

@app.route('/adminlogout')
def admin_logout():
    return render_template('index.html')
@app.route('/food_delete', methods=['POST'])
def food_delete():
 
    id= request.form.get('id')
   
    
    db.delete_food(id)
    
    return render_template('delete_sucsess.html')

@app.route('/foodsearchinput')
def food_search_input():
    return render_template('food_search.html')

@app.route('/userfoodsearchinput')
def user_food_search_input():
    return render_template('ufood_search.html')






#ユーザー関連


@app.route('/', methods=['GET'])
def index():
    msg = request.args.get('msg')
    
    if msg == None:
        return render_template('index.html')
    else:
        return render_template('index.html', msg = msg)
    
@app.route('/', methods=['POST'])
def login():
    username = request.form.get('username')
    mail = request.form.get('mail')
    password = request.form.get('password')
    
    if db.login(username, mail,password):
        session['user'] = True
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=100)
        
        return redirect(url_for('mypage'))
    else:
        error = 'ログインに失敗しました。'
        input_data  = {
            'username': username,
            'mail': mail,
            'password': password
        }
        return render_template('index.html', error = error, data = input_data)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/mypage', methods=['GET'])
def mypage(): 
    
    if 'user' in session:
        return render_template('mypage.html')
     
    else:
        return redirect(url_for('index'))
    
@app.route('/register')
def register_form():
    return render_template('register.html')

@app.route('/register_exe', methods=['POST'])
def register_exe():
    user_name = request.form.get('username')
    mail = request.form.get('mail')
    password = request.form.get('password')
    
    if user_name == '':
        error = 'ユーザー名が未入力です。'
        return render_template('register.html', error = error)
    if password == '':
        error = 'パスワードが未入力です。'
        return render_template('register.html', error = error)
    
    count = db.insert_user(user_name, mail,password)
    
    if count == 1:
        msg = '登録が完了しました。'
        return render_template('index.html', msg=msg)
    else:
        error = '登録に失敗しました。'
    return render_template('register.html', error=error)

@app.route('/list')
def sample_list():
    touroku_list = db.select_all_touroku()
    return render_template('list.html', touroku=touroku_list)

@app.route('/sample_register')
def sample_register():
    return render_template('touroku.html')

if __name__ == "__main__":
    app.run(debug=True)

#-----------------------------------------------------------------------------
@app.route('adminlogin', methods=['POST'])
def adminlogin():
    username = request.form.get('username')
    mail = request.form.get('mail')
    password = request.form.get('password')
    
    if db.login(username, mail,password):
        session['user'] = True
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=100)
        
        return redirect(url_for('admintopmenu'))
    else:
        error = 'ログインに失敗しました。'
        input_data  = {
            'username': username,
            'mail': mail,
            'password': password
        }
        return render_template('index.html', error = error, data = input_data)


@app.route('/admintopmenu', methods=['GET'])
def admintopmenu(): 
    
    if 'user' in session:
        return render_template('admin_topmenu.html')
     
    else:
        return redirect(url_for('index'))

