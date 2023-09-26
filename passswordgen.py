import random 
import string 


def pass1(m):
    #all type of characters
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
    #only letters,digits and uppercase
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
def pass7(l):
    #only lowercase
    password=[random.sample(string.ascii_lowercase,l)]
    passwordstr=''.join(password)
    print(passwordstr)
    return

def pass3(o):
    #only letters and uppercase
    letters_=string.ascii_letters
    password=[random.choice(string.ascii_uppercase)]
    length_left= int(l) -1
    c=random.sample(letters_,length_left)

    password.extend(c)

    passwordstr="".join(password)
    print(passwordstr)
    return
def pass6(v):
    #only letters and numbers
    letters_=string.ascii_letters
    digits_=string.digits
    mix=[letters_+digits_]

    password=random.sample(mix,v)
    password.str="".join(password)
    print(passwordstr)
    return

def pass4(p):
    #only letters and special characters
    letters_=string.ascii_letters
    special_=random.choice(["!","@",'+','=','-','_','#','$','%','^','&','*'])
    password=[special_]
    lengthleft=int(p) - 1
    d=random.sample(letters_,lengthleft)
    password.extend(d)
    passwordstr=''.join(password)
    print(passwordstr)
    return

def pass5(l):
    #only letters
    password=random.sample((string.ascii_letters),l)
    passwordstr="".join(password)
    print(passwordstr)
    return
def pass8(x):
    #letters, numbers and special charcs
    letters_=string.ascii_letters
    special_=random.choice(["!","@",'+','=','-','_','#','$','%','^','&','*'])
    digits_=string.digits
    strin=[letters_,digits_]
    password=[random.choice(special_)]
    lengthleft= int(x) - 1
    strin2=random.sample(strin,lengthleft)
    password.extend(strin2)
    passwordstr="".join(password)
    print(passwordstr)
    return

while True:
    print("Password Generator")
    l=int(input("How long do you want the password to be? (Enter a digit between 4-20)\n"))
    if l>=4 and l<=20:
        
        a=str.lower(input("Do you want to include Uppercase alphabets? \n"))
        if a==("yes" or "y"):
            b=str.lower(input("Do you want to include numbers?\n"))
            if b==("yes" or "y"):
                c=str.lower(input("Do you want to include special characters?\n"))
                if c==("yes" or"y"):
                    pass1(l)
                    break
                elif c==("no" or 'n'):
                    pass2(l)
                    break
                else:
                    print("Invalid input")
                    exit(0)
            elif b==("no" or 'n'):
                 d=str.lower(input("Do you want to include special characters?\n"))
                 if d==("yes" or "y"):
                     pass4(l)
                     break
                 elif d==("no" or "n"):
                     pass3(l)
                     break
                 else:
                     print("invalid input")
                     exit(0)
            else:
                print("Invalid input")
        elif a==("no" or "n"):
            b=str.lower(input("Do you want to include numbers?\n"))
            if b==("yes" or "y"):
                  c=str.lower(input("Do you want to include special characters?\n"))
                  if c==("yes" or "y"):
                      pass8(l)
                      break
                  elif c==("no" or "n"):
                      pass6(l)
                      break
                  else:
                      print("Invalid input")
                      exit(0)
            elif b==("no" or "n"):
                 c=str.lower(input("Do you want to include special characters?\n"))
                 if c==("yes" or "y"):
                     pass4(l)

                     break
                 elif c==("no" or "n"):
                     pass7(l)
                     break
                 else:
                     print("Invalid Input")
                     exit(0)
            else:
                print("Invalid input")
                exit(0)
        else:
            print("Invalid input")
            exit(0)


    else:
        print("Please enter a value within the specified range")
        exit(0)
