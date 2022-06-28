#!/usr/local/bin/python3.8
print("Content-Type:text/html\r\n\r\n")

# --------------modules-------------
import mysql.connector as msc


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

try:
    mydb = msc.connect(host="sql6.freemysqlhosting.net",user="sql6501859",password="sirf1shlki",port="3306")
    mycursor = mydb.cursor()
    mycursor.execute('use website')
except:
    print('<script>alert("database connectivity error! 1");</script>')

try:
    mycursor.execute("DELETE FROM USER WHERE email='{}' and password='{}'".format(userEmail,userPassword))
    mycursor.execute('commit')
except:
    print('<script>alert("database connectivity error! 2");</script>')

try:
    fp = open("/var/www/cgi-bin/userEmail.txt","w")
    fp.close()
    fp = open("/var/www/cgi-bin/userPassword.txt","w")
    fp.close()
    print("<script>window.open('http://localhost/cgi-bin/login.py','_self');</script>")
except:
    print('<script>alert("DataBase Error !")</script>')
