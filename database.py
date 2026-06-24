
import sqlite3
def init_db():
    conn=sqlite3.connect('sentinel.db')
    conn.execute('create table if not exists alerts(id integer primary key, threat text)')
    conn.commit()
    conn.close()
