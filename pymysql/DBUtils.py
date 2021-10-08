import pymysql

host = 'localhost'
user = 'root'
password = ''
database = 'bank'

def close(con, cur):
    con.commit()
    cur.close()
    con.close()

def update(sql, params):
    connect = pymysql.connect(host=host, user=user, password=password,
                              database=database, charset='utf8')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, params)
    close(connect, cursor)

def query(sql, parmas=[], size=0):
    connect = pymysql.connect(host=host, user=user, password=password,
                              database=database, charset='utf8')
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, parmas)
    if size == 0:
        return cursor.fetchall()
    elif size == 1:
        return cursor.fetchone()
    else:
        return cursor.fetchmany(size)
    close(connect, cursor)