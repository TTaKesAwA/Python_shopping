import os, psycopg2, string, random, hashlib


def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def select_all_foods():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = 'SELECT * FROM food ORDER BY id ASC;'
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

def edit_food(id,name,make,worth,stock):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'UPDATE food SET name= %s, make= %s, worth= %s, stock= %s WHERE id = %s'
    
    cursor.execute(sql,(name,make,worth, stock,id))
    
    count = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return count

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

def search_food(keyword):
    connection = get_connection()
    connection.cursor()
    cursor = connection.cursor()
    sql = 'SELECT * FROM food WHERE name LIKE %s'
    print('キーワード：'+keyword)
    keyword='%'+keyword+'%'
    cursor.execute(sql,(keyword,))
    
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

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




#ユーザー関連


def get_salt():
    charset =string.ascii_letters + string.digits
    salt = ''.join(random.choices(charset, k=30))
    return salt

def get_hash(password, salt):
    b_pw = bytes(password, 'utf-8')
    b_salt = bytes(salt, 'utf-8')
    hashed_password = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 1000).hex()
    return hashed_password
    
    
def insert_user(user_name, mail,password):
    sql = 'INSERT INTO ecuser VALUES(default, %s, %s, %s,%s)'
    
    salt = get_salt()
    hashed_password = get_hash(password, salt)

    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(sql, (user_name, mail,salt,hashed_password,))
        count = cursor.rowcount #更新件数を取得
        connection.commit()
        
    except psycopg2.DatabaseError:
        count = 0
    finally:
        cursor.close()
        connection.close()
        
    return count

def login(user_name, password):
    sql = 'SELECT hashed_password, salt FROM customer WHERE name = %s' #ユーザー名がに件取れる可能性があるから直すnmae=%sのとこ
    flg = False

    try :
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_name, ))
        user = cursor.fetchone()

        if user != None:
            salt = user[1]

            hashed_password = get_hash(password, salt)

            if hashed_password == user[0]:
                flg = True
    except psycopg2.DatabaseError:
        flg = False
    finally :
        cursor.close()
        connection.close()
    
    return flg