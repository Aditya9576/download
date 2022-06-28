#!/usr/local/bin/python3.8
print("Content-Type:text/html\r\n\r\n")

#-------------html header-----------------
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head><title>MyAccount</title></head>')
print('<link rel="stylesheet" href="http://localhost/header_footer.css" />')
print('<link rel="stylesheet" href="http://localhost/myAccount_css.css" />')
print('<body>')
print(' <div id="header_nav">')
print('<div class="menu">')
print('<ul style="list-style-type:none">')
print('<a href="http://localhost/index.html" target="_self"><li>HOME</li></a>')
print('<a href="#"><li>SHOP</li></a>')
print('<a href="#"><li>PRODUCT</li></a>')
print('<a href="#"><li>PAGES</li></a>')
print('<a href="#"><li>SITEMAP</li></a>')
print('<a href="http://localhost/about.html" target="_blank"><li>ABOUT</li></a>')
print(' </ul>')
print('</div>')
print('<div class="search_bar">')
print('<input type="text" placeholder="Search Products" /> <span style="font-size:20px;">&#x1F50D</span>')
print('&nbsp;&nbsp;&nbsp;&nbsp;')
print('<a href="#footer"> <div class="basic_icons" ><center> &downarrow;</center></div></a>')
print('</div>')
print('</div>')

# -------------deatils box-------------- 

print('<div class="container">')
print('<div class="personal_info">')
print('<p>Personal Info &nbsp;&nbsp;&nbsp;<span style="font-size:0.8em;font-weight:normal;cursor:pointer;" onclick="enable_info()">Edit&nbsp;&#128393;<span></p>')
print('<form action="http://localhost/cgi-bin/myAccount_insert.py">')
print('<input type="text" name="fname" placeholder="Aditya" id="name" disabled/>')
print('<input type="text" name="lname" placeholder="Raj" disabled/></br></br>')
print('<p>LogIn Credential</p>')
print('<label>Email Address</label> </br>')
print('<input type="email" name="email" disabled/></br>')
print('<label>Password</label> </br>')
print('<input type="password" name="password" id="pass" disabled/>&nbsp;<span style="cursor:pointer;font-size:1.3em;border:none;outline:none;" onclick="showPassword()">&#x1F441;</span></br></br>')
print('<p>Address</p>')
print('<span>Mobile Number</span></br>')
print('<input type="number" name="mobile" disabled/></br></br>')
print('<span>Address Line 1</span></br>')
print('<input type="text" name="address1" disabled/> </br></br>')
print('<span>Address Line 2</span></br>')
print('<input type="text" name="address2" disabled/></br></br>')
print('<input type="submit" value="SAVE" id="save3" disabled/>')
print('</form>')
print('</div>')
print('<div class="faqs">')
print('<p style="font-weight:bold;font-style:sans-serif;font-size:1.5em;color:black;">FAQs</p>')
print('<div class="faq_details">')
print('<span>What happens when I update my email address (or mobile number)?</span></br>')
print('Your login email id (or mobile number) changes, likewise. You will receive all your account related communication on your updated email address (or mobile number).')
print('</br><span>When will my account be updated with the new email address (or mobile number)?</span></br>')
print('It happens as soon as you confirm the verification code sent to your email (or mobile) and save the changes.')
print('</br><span>What happens to my existing account when I update my email address (or mobile number)?</span></br>')
print("Updating your email address (or mobile number) doesn't invalidate your account. Your account remains fully functional. You'll continue seeing your Order history, saved information and personal details.")
print('</br><span>Does my Seller account get affected when I update my email address?</span></br>')
print("This site has a 'single sign-on' policy. Any changes will reflect in your Seller account also.")
print('</div></br></br>')
print('<a href="http://localhost/cgi-bin/deactivate_account.py" target="_self"><p style="font-family:sans-serif;color:red;cursor:pointer;">Deactivate Account</p></a>')

#--------------------footer--------------------
print('<h2 class="footer_head">ACCOUNT SETTINGS</h2>')
print('<div id="footer">')
print('<ul style="list-style-type:none">')
print('<li style="font-weight:bold;font-size:2em;font-family:sans-serif;line-height:90px;border:none;cursor:text;">About</li>')
print('<a href="http://localhost/cgi-bin/authenticate.py" target="_self"><li>My account</li></a>')
print('<a href="http://localhost/about.html" target="_blank"><li>About</li></a>')
print('<a href="#"><li>Sitemap</li></a>')
print('<a href="#"><li>Product</li></a>')
print('</ul>')
print('<ul style="list-style-type:none">')
print('<li style="font-weight:bold;font-size:2em;font-family:sans-serif;line-height:90px;border:none;cursor:text;">Information</li>')
print('<a href="http://localhost/register.html" target="_self"><li>Register</li></a>')
print('<a href="http://localhost/login.html" target="_self"><li>Login</li></a>')
print('<a href="#"><li>My Cart</li></a>')
print('<a href="#"><li>Wishlist</li></a>')
print('<a href="http://localhost/cgi-bin/logout.py"> <li style="color:red;">LogOut</li></a>')
print('</ul>')
print('<div class="subscribe">')
print('<div class="subscribe_details">')
print('<p style="font-size:2em;font-weight:bolder;font-family:sanf-serif;">Do not miss a thing</p>')
print('<p style="font-family:sanf-serif;"> Enter your email below to be the first to know about new </br> collections and product launches.</p>')
print('</div>')
print('<form class="footer_form">')
print('<div class="email_logo">&#9993;</div>')
print('<input type="email" placeholder="Enter your email">')
print('<button type="submit">&rightarrow;</button>')
print('</form>')
print('</div>')
print('</div>')
print('<hr>')
print('</body>')
print('<script src="http://localhost/myAccount_script.js"></script>')
print('</html>')
# --------------modules-------------
import cgi
import mysql.connector as msc

#-------------database connectivity-------------
try:
    mydb = msc.connect(host="sql6.freemysqlhosting.net",user="sql6501859",password="sirf1shlki",port="3306")
    mycursor = mydb.cursor()
    mycursor.execute('use website')
except:
    print('<script>alert("database connectivity error!")</script>')


cg = cgi.FieldStorage()

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

#-------------- find useEmail & password in database----------------
try:
    if fp != "null":
        mycursor.execute("SELECT * FROM USER WHERE email ='{}' and password = '{}'".format(userEmail,userPassword))
        cursorList = mycursor.fetchall()
        print('<script>')
        print('document.getElementsByTagName("input")[1].value="{}"'.format(cursorList[0][0]))
        print('document.getElementsByTagName("input")[2].value="{}"'.format(cursorList[0][1]))
        print('document.getElementsByTagName("input")[3].value="{}"'.format(cursorList[0][4]))
        print('document.getElementsByTagName("input")[4].value="{}"'.format(cursorList[0][5]))
        print('document.getElementsByTagName("input")[5].value="{}"'.format(cursorList[0][3]))
        print('document.getElementsByTagName("input")[6].value="{}"'.format(cursorList[0][6]))
        print('document.getElementsByTagName("input")[7].value="{}"'.format(cursorList[0][7]))
        print('</script>')
    else:
        print('<script>alert("hello")</script>')
except:
    print('<script>alert("ERROR!! contact developer")</script>')
