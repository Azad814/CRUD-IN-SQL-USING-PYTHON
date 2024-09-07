# Create, read, Update, Delete 
import mysql.connector


#Connecting to mysql database
try:
    conn= mysql.connector.connect(
        host="127.0.0.1",
        user= "root",
        password="######",
        database = 'crud_python'
    )
    mycursor= conn.cursor() 
    print('Connection Established');
except:
    print('Connection Error');


#Create a database  
#$mycursor.execute('create database crud_python_2')
conn.commit()
print('database created')


#Create Table 
'''mycursor.execute("""create table customer
                    (id integer primary key,
                    name varchar(50) not null,
                    email varchar(50) not null,
                    age integer)""")'''
conn.commit()
print('table is created')

#inserting values into the table
'''mycursor.execute(
    """insert into customer values 
        (1, 'Anil', 'anil@gmail.com', 40),
    (2,'rahul', 'sdfsds', 23),
    (3, 'asas', 'adass@', 46)
    """
)
conn.commit()
print('rows are inserted')'''

#reading the values in the table 
mycursor.execute('select * from customer')
myresult= mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)


#update data in table 
mycursor.execute('update customer set age =40 where id=1')
conn.commit()
print('updated')

mycursor.execute('select * from customer')
myresult= mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)


#delete data from the table 
mycursor.execute('delete from customer where id=1')
conn.commit()
print('deleted')
mycursor.execute('select * from customer')
myresult= mycursor.fetchall()
print(myresult)
for x in myresult:
    print(x)