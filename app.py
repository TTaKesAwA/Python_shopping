from flask import Flask, render_template
from food import food_bp
from d_item import d_item_bp

app = Flask(__name__)
app.register_blueprint(food_bp)
app.register_blueprint(d_item_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


