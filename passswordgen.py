import random 
import string 
def passt(m):
    letters_=string.ascii_letters
    digits_=string.digits
    uppercase_=random.choice(string.ascii_uppercase)
    special_=random.choice(["!","@",'+','=','-','_','#','$','%','^','&','*'])

    
    password=[special_+ uppercase_]
    lengthleft= int(l)-2
    charcs=letters_ + digits_
    
    charcs2=random.sample(charcs,lengthleft) 

    password.extend(charcs2)
    
    passwordstr="".join(password)
    print(passwordstr)
    return


l=input("How long do you want the password to be? \n 1. 8 Characters long \n 2. 10 Characters long \n 3. 16 Characters long \n")
passt(l)


