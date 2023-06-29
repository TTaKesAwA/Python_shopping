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

def insert_food(name,make,worth):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO food VALUES (default, %s, %s, %s)'
    
    cursor.execute(sql,(name,make,worth))
    
    count = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return count
   