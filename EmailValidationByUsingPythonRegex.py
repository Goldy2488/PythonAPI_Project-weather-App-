import re
email_condtion = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your Email : ")

if re.search(email_condtion,user_email):
    print("Right Email😉")
else: print("wrong Email ")