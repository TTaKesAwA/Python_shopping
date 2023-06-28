import psycopg2

def aaaaa(key):
    connection = psycopg2.connect(user='postgres',
                              password= 'Jyobijyobi1142',
                              host='localhost',
                              database='postgres')

    cursor = connection.cursor()

    sql = "SELECT * FROM food"
    key = '%' + key + '%'
    cursor.execute(sql(key,))

    rows = cursor.fetchall()
    row = cursor.fetchone()
    result = []
    for row in rows:
        result.append(row[1])

    cursor.close()
    connection.close()
    return result
user_list=aaaaa('i')
print(user_list)