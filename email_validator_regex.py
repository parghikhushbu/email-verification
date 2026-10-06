# a-z wscube@gmail.com 
# 0-9 
# . _ time 1
# @ time 1
# . 2,3
import re
email_condition="^[a-z]+[\._]?[a-z 0-9 ]+[@]\w+[.]\w{2,3}$"#+ mean merge
#alphabet start with a to z , _ . at a time one used , ? at a one vovu joye , 
#0 - 9 digits group of number , @ special character \w , . search [2,3]position , at last search $
user_email=input("Enter your Email : ")
if re.search(email_condition,user_email):
    print(" Right Email ")
else:
    print(" Wrong Email ")



