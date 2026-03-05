import pyfiglet

f_hash = input("Enter first hash: ")
s_hash = input("Enter second one: ")
f = f_hash.replace(" ", "")
s = s_hash.replace(" ", "")

if f == s:
    print(pyfiglet.figlet_format("File is safely received!", font="slant"))
else :
    print(pyfiglet.figlet_format("This file is changed and it is not safe!", font="slant"))
