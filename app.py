from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)


