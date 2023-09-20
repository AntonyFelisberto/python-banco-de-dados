import sqlite3

#conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("customer.db")

c = conn.cursor()

#sqlite has three types NULL,INTEGER,REAL,TEXT,BLOB
c.execute("""
          CREATE TABLE customers( 
            first_name text,\
            last_name text,\
            email text\
          )""")
conn.commit()

c.execute("INSERT INTO customers (first_name,last_name,email) VALUES ('ARTORIAS','SORI','AKRWS@job.com')")
conn.commit()

f,l,e = "ant","rts","nnnn@email.com"
c.execute("INSERT INTO customers (first_name,last_name,email) VALUES (?,?,?)",(f,l,e))
conn.commit()

many_customers = [("wes","brown","awsd@job.com"),("wes","weasr","awsd@jobww.com"),("mono","brown","awsd@job.com")]
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
conn.commit()

c.execute("SELECT * FROM customers")
print(c.fetchone()) #PRA CADA EXECÇÃO TEM QUE TER UM EXECUTE SENÃO NÃO FUNCIONA SENDO DELEE,FETCH ETC

c.execute("SELECT * FROM customers")
print(c.fetchone()[0])

c.execute("SELECT * FROM customers")
print(c.fetchmany(3))

c.execute("SELECT * FROM customers")
print(c.fetchall())

items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers WHERE first_name = 'ARTORIAS' OR first_name like '%A%'")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers WHERE first_name = 'ARTORIAS' AND email like '%@job.com'")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers ORDER BY rowid")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers ORDER BY rowid DESC")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers ORDER BY last_name")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers ORDER BY last_name DESC")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT first_name FROM customers LIMIT 2")
items = c.fetchall()
for item in items:
    print(item)

c.execute("""
    UPDATE customers SET last_name = 'IZUKU' WHERE rowid = '2'
""")

c.execute("DELETE FROM customers WHERE rowid = 6;")
conn.commit()

id = 2
c.execute("DELETE FROM customers WHERE rowid = (?);",id)
conn.commit()

c.execute("DROP TABLE customers;")
conn.commit()


conn.close()