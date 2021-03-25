""" Functions :- function is a set of statements or block 
    of executable code usualy starts with def keyword 
    def - means defining the function """
    
def function():
    print("hello")
    print("where are you?")
print("I am outside") 

def function1(x):
    
     print(x)
     print("I am still here")
     return x*3 
 
def function2(x,y):
    print("Addition is simple")
    return x+y 

function()

a=function1(2)
print(a)

b=function1(4)
print(b)

c=function2(2,3)
print(c)

name1 = "sam"
height1 = "2"
weight1 = "82"

name2 = "sam's brother"
height2 = "2.2"
weight2 = "90"

name3 = "sam's sister"
height3 = "1.8"
weight3 = "120"

def bmi_calc(name,height,weight):
    bmi =( weight / height) 
    print("bmi :-")
    print(bmi)
    if bmi < 25:
        return name+ " is not overweight"
        
    else:
        return name+" is overweight"
        
#bmi_calc(name,height,weight) 
        
result1 = bmi_calc(name1, height1, weight1) 
result2 = bmi_calc(name2, height2, weight2)
result3 = bmi_calc(name3, height3, weight3)

print(result1)
print(result2)
print(result3)   
   