'''
Created on Jan 19, 2021

@author: kulkarnivasanti
'''
def get_integer():
    return int(input("Enter the number"))

age  = get_integer()
grade = get_integer()

if age>15:
    print("you are in high school")
    print("you are in the grade "+str(grade))
    
def get_country():
    return str(input("Enter the name of country"))

country = get_country()

if country=="china":
    print("you are asian")
else:
    print("you are not asian")    