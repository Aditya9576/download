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
phone = cg.getvalue("mobile")
address1 = cg.getvalue('address1')
address2 = cg.getvalue("address2")

try:
    mydb = msc.connect(host="sql6.freemysqlhosting.net",user="sql6501859",password="sirf1shlki",port="3306")
    mycursor = mydb.cursor()
    mycursor.execute('use website')
except:
    print('<script>alert("database connectivity error!")</script>')

#------------ open user and password file-----------------
try:
    fp = open("/var/www/cgi-bin/userEmail.txt","r")
    userEmail = fp.read();
    fp.close()
    try:
        fp = open("/var/www/cgi-bin/userPassword.txt","r")
        userPassword = fp.read();
        fp.close()
    except:
        fp = "null"
        print(fp)
except:
    fp = "null"
    print('<b style="color:red;">{}</b>'.format(fp))

#-------------- insert data in database----------------
try:
    if fp != "null":
        mycursor.execute("UPDATE USER SET fname='{}' , lname='{}' ,phone='{}' , address1='{}' , address2='{}' WHERE email='{}' and password='{}'".format(fname,lname,phone,address1,address2,userEmail,userPassword))
        mycursor.execute("commit")
        print("<script>window.open('http://localhost/cgi-bin/myAccount_display.py','_self');</script>")
except:
    print('<script>alert("ERROR!! contact developer")</script>')