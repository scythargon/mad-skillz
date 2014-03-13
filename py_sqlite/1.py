from pysqlite2 import dbapi2 as sqlite

con = sqlite.connect('users.db')
cur = con.cursor()
#cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, firstName VARCHAR(100), secondName VARCHAR(30))')
#con.commit()
#cur.execute('INSERT INTO users (id, firstName, secondName) VALUES(NULL, "Guido", "van Rossum")')
#con.commit()
#print cur.lastrowid
#cur.execute('SELECT * FROM users')
#cur.execute('select name from sqlite_master')

cur.execute('drop table if exists notes')
cur.execute('drop table if exists sites')
cur.execute('CREATE TABLE sites (id INTEGER PRIMARY KEY, site_name TEXT, theme_color TEXT)')
cur.execute("""CREATE TABLE notes (id INTEGER PRIMARY KEY, site integer, text TEXT, FOREIGN KEY(site) REFERENCES artist(id))""")
cur.execute('select name from sqlite_master')
print cur.fetchall()


