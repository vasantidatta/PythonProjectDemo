'''
Created on Jan 17, 2021

@author: kulkarnivasanti
'''

class Sets_Basics:
    
    fruits = {"apple","banana","cherry","dragonfruit","grape","jackfruit"}
    fruits2 = {"cherry","blackberry","crainberry","blueberry","strawberry"}
    
    for x in fruits:
        print(x)
        

    print("banana" in fruits)  
    
    fruits.add("orange")  
    
    print(fruits)
    
    fruits.update(fruits2)
    print(fruits)
    
    
    
    
''