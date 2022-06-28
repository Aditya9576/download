#!/usr/local/bin/python3.8
print("Content-Type:text/html\r\n\r\n")

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
        print('<script>alert("PASSWORD  ERROR !")</script>')
except:
    print('<script>alert("Email  ERROR !")</script>')

if len(userEmail)!=0:
    print("<script>window.open('http://localhost/cgi-bin/myAccount_display.py','_self');</script>")
else:
    print("<script>window.open('http://localhost/login.html','_self');</script>")
