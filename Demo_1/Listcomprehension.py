# List comprehension : returns the new list with particular elements

Fruits = ['apple','banana','cherry','fig','mango','orange','pear','starfruit']
Fruits1 = []
Fruits2 = []
Fruits3 = []

print(Fruits)

for x in Fruits:
    if 'a' in x:
        Fruits1.append(x)
        
print("1) ",Fruits1) 

for y in Fruits:
    if 'e' in y:
        Fruits2.append(y)
               
print("2) ",Fruits2)

for z in Fruits:
    if 'r'in z:
        Fruits3.append(z)
        
print("3) ",Fruits3)    

a = [x for x in Fruits if x!="apple"]
print("Apple not included ",a)

b = [y for y in Fruits if y!="banana"]
print("banana not included ",b)







