import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","alohomora93/4","Cricket" )

# prepare a cursor object using cursor() method
a = db.cursor()
b = db.cursor()
sql = 'select * from cricket;'
s = 'select Player from cricket where category= "Bat";'

# execute SQL query using execute() method.

a.execute(s)
b.execute(sql)
# Fetch a single row using fetchone() method.
data = a.fetchall()
data2 = b.fetchall()
print (data)
print(data2)
# disconnect from server
db.close()



