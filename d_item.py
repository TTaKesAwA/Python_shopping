from flask import Blueprint, render_template

d_item_bp = Blueprint('d_item', __name__, url_prefix='/d_item')

@d_item_bp.route('/list')
def d_item_list():
  
    d_item_list = [
         ('歯ブラシ', '東京',  100),
        ('ティッシュ', '埼玉', 300),
    ]
    
    return render_template('d_item/list.html', d_items=d_item_list)