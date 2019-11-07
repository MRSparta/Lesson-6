import pyodbc

# Variables to connect to DB

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# what is a cursor?

cursor = docker_northwind.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row)

#we can also Fecthc all rows
#all_customer=cursor.execute ('SELECT * FROM Customers;').fetchall()
#Fetch all is dangerous as it can block our CPU with huge amount of data
#print(all_customer)
#print(type(all_customer))
#for row in all_customer:
  #do operation with data.
  #print row.ContactName, row.Fax)
#Because this is dangerous we can use while loop to fecthone()
#until record/ row is none --> break
#all_products=cursor,execute('SELECT * FROM Products;')
#this is more efficient than fectchall()
#while True:
#row_record = all_products.fetchone()
   #if row_record is None:
   #break
   #print(row_record.unitprice)



# all_customers = cursor.excute("SELECT * FROM Customers;").fetchall()
# Fetch