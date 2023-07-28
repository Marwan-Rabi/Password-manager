import sqlite3
conn = sqlite3.connect('passman.db')
c = conn.cursor()
#site url - email - password
# c.execute("""CREATE TABLE passmanager(
#     site_url text,
#     email text,
#     password
# )         """)

#SELECT function
def SELpass(siteurl):
    conn = sqlite3.connect('passman.db')
    c = conn.cursor()
     
    sql = (""" SELECT site_url,email,password FROM passmanager
              WHERE site_url = ? """)
    c.execute(sql, [siteurl])
    
    items = c.fetchall()
    for i in items:
        print(i)

    conn.commit()
    conn.close()
# #INSERT function   
def INSpass(siteurl,email,password):
      conn = sqlite3.connect('passman.db')
      c = conn.cursor()
      
      c.execute(""" INSERT INTO passmanager
        (site_url,email,password)        
        VALUES(?,?,?)""", (siteurl,email,password))
      conn.commit()
      conn.close()
# DELETE function
def DELpass(emails):
    conn = sqlite3.connect('passman.db')
    c = conn.cursor()
    
    dsql = ("DELETE FROM passmanager WHERE email = ?")
    c.execute(dsql,[emails])
    conn.commit()
    conn.close()


#UPDATE Function
def UPDpass(password, emails):
    conn = sqlite3.connect('passman.db')
    c = conn.cursor()
    
    usql = (""" UPDATE passmanager SET password = ? WHERE email = ?""")
    c.execute(usql, [emails,password])
    
    conn.commit()
    conn.close()
def smallfunc():
    conn = sqlite3.connect('passman.db')
    c = conn.cursor()
    ssql = ("SELECT * FROM passmanager ORDER BY rowid DESC LIMIT 1")
    c.execute(ssql)
    items = c.fetchall()
    for i in items:
        print(i)
    conn.commit()
    conn.close()



