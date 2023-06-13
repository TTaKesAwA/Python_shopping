from flask import Blueprint, render_template

food_bp = Blueprint('item', __name__, url_prefix='/item')

@food_bp.route('/list')
def d_item_list():
  
    d_item_list = [
         ('歯ブラシ', '東京',  100),
        ('ティッシュ', '埼玉', 300),
    ]
    
    return render_template('item/list.html', d_items=d_item_list)