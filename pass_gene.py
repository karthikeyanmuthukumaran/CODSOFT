#Program about Password_Generator
import random
import string

#user input getting
length=int(input("enter the lenght of password:"))

lower_length=int(input("enter number of lower_case letter you want:"))
upper_lenght=int(input("enter number of upper_case letter you want:"))
symbol_lenght=int(input("enter number of symbol length you want:"))
digit_length=int(input("enter no of digit lenght you want :"))

pass_length=lower_length+upper_lenght+symbol_lenght+digit_length

#using ACSII to get all variables
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

all_string=random.choices(lower,k=lower_length)+random.choices(upper,k=upper_lenght)+random.choices(symbols,k=symbol_lenght)+random.choices(digits,k=digit_length)
pwd=random.sample(all_string,length)
password="".join(pwd)

print("the password is:",password)