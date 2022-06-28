#!/usr/local/bin/python3.8
print("Content-Type:text/html\r\n\r\n")

# --------------modules-------------
import cgi
import mysql.connector as msc

cg = cgi.FieldStorage()
fname = cg.getvalue("fname")
lname = cg.getvalue("lname")
email = cg.getvalue("email")
password = cg.getvalue("password")
sex = "...."
phone = "....."
address1 = "....."
address2 = "....."

try:
    mydb = msc.connect(host="sql6.freemysqlhosting.net",user="sql6501859",password="sirf1shlki",port="3306")
    mycursor = mydb.cursor()
    mycursor.execute('use website')
except:
    print('<script>alert("database connectivity error!");</script>')


try:
    mycursor.execute("SELECT * FROM USER WHERE email='{}'".format(email))
    listLenghth = mycursor.fetchall()
    if len(listLenghth)!=0:
        print("<script> alert('Accout with this Email already exist ! Try Login or use another Email!')</script>")
        print("<script>window.open('http://localhost/register.html','_self');</script>")
    else:
        try:
            mycursor.execute("INSERT INTO USER (fname,lname,sex,phone,email,password,address1,address2) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,lname,sex,phone,email,password,address1,address2))
            mycursor.execute("commit")
            print("<script>alert('Account Created');</script>")
            print("<script>window.open('http://localhost/login.html','_self');</script>")
        except:
            print('<script> alert("database error!")</script>')
except:
    print('<script>alert("database connectivity error!")</script>')
    
        