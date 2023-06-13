from flask import Blueprint, render_template

food_bp = Blueprint('food', __name__, url_prefix='/food')

@food_bp.route('/list')
def food_list():
  
    food_list = [
         ('魚', '三陸',  100),
        ('ネギ', '群馬', 100),
    ]
    
    return render_template('food/list.html', foods=food_list)