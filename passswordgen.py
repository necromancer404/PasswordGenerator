import random 
import string 


def pass1(m):
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
def pass2(n):
    letters_=string.ascii_letters
    digits_=string.digits
    password=[random.choice(string.ascii_uppercase)]
    lengthleft= int(l)-1
    charcs=letters_ + digits_
    charcs2=random.sample(charcs,lengthleft)
    password.extend(charcs2)
    passwordstr="".join(password)
    print(passwordstr)
    return
def pass3(o):
    letters_=string.ascii_letters
    password=[random.choice(string.ascii_uppercase)]
    length_left= int(l) -1
    c=random.sample(letters_,length_left)

    password.extend(c)

    passwordstr="".join(password)
    print(passwordstr)
    return
while True:
    l=int(input("How long do you want the password to be? (Enter a digit between 4-20)\n"))
    if l>=4 and l<=20:
        print("Password Generator")
        a=input("Do you want to include Uppercase alphabets? \n")
        if a=="yes":
            b=input("Do you want to include numbers?\n")
            if b=="yes":
                c=input("Do you want to include special character?\n")
                if c=="yes":
                    pass1(l)
                    break
                else:
                    pass2(l)
                    break
            else:
                pass3(l)
                break
        else:
            print("Error with your input")
            exit(0)
    else:
        print("Please enter a value within the specified range")

        



