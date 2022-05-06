import __main__
import mysql.connector

sql_user = 'USERNAME'
sql_pass = 'PASSWD'

host= 'localhost'
database = 'virusshare'

def find_hash(hash):
    print('starting hash search')

    db = mysql.connector.connect(user='{}'.format(sql_user),
                                 password='{}'.format(sql_pass),
                                 host='{}'.format(host),
                                 database='{}'.format(database),
                                 auth_plugin='mysql_native_password')
    c = db.cursor()
    c.execute('''
    SELECT hash FROM sig WHERE hash='%s'
    '''%(hash))
    try:
        print(__main__._sql_server)
        __main__.q.put(c.fetchone()[0])
        print('done')
    except:
        __main__.q.put('None')



def insert_new_hash(hash):
     
    db = mysql.connector.connect(user='{}'.format(sql_user),
                                 password='{}'.format(sql_pass),
                                 host='{}'.format(host),
                                 database='{}'.format(database),
                                 auth_plugin='mysql_native_password')
    c = db.cursor()
    c.execute(' INSERT INTO bad_hash (id, hash) VALUES (default, "%s");' % hash)
    db.commit()

def get_count_hash():
    db = mysql.connector.connect(user='{}'.format(__main__._sql_user),
                                 password='{}'.format(__main__._sql_hashdb),
                                 host='{}'.format(__main__._sql_server),
                                 database='{}'.format(__main__._sql_hashdb))
    c = db.cursor()
    c.execute('''
    SELECT COUNT(*) FROM sig
    ''')
    print('ended')

    return c.fetchone()[0]


def remove_hash(hash):
    db = mysql.connector.connect(user='{}'.format(__main__._sql_hashdb),
                                 password='{}'.format(__main__._sql_hashdb),
                                 host='{}'.format(__main__._sql_server),
                                 database='{}'.format(__main__._sql_hashdb))
    c = db.cursor()
    c.execute('''
    DELETE FROM sig WHERE hash="{}"
    '''.format(hash))
    db.commit()


def update():
    print('asdf')

