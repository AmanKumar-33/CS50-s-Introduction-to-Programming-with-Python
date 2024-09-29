import re
email = input("enter your email:-").rstrip()



if re.search(r".+@.+\.edu",email):
    print("valid")
else:
    print("invalid")
