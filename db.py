import os
import psycopg2

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def select_all_foods():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = 'SELECT * FROM food'
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

def insert_food(name,make,worth,stock):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO food VALUES (default, %s, %s, %s, %s)'
    
    cursor.execute(sql,(name,make,worth, stock))
    
    count = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return count
def search_food(id,name,make):
    connection = get_connection()
    connection.cursor()
    cursor = connection.cursor()
    sql = 'SELECT * FROM food WHERE id like %s OR name like %s OR make like %s'
    
    cursor.execute(sql,(id,name,make))
    
    count = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return count

def delete_food(id):
    connection = get_connection()
    connection.cursor()
    cursor = connection.cursor()
    sql = 'DELETE FROM food WHERE id = %s'
    
    cursor.execute(sql,(id))
    
    count = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return count

