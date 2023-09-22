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


while True:
    l=int(input("How long do you want the password to be? (Enter a digit between 4-20)\n"))
    if l>=4 and l<=20:
        passt(l)
        break
    else:
        print("Please enter a value within the specified range")

        



