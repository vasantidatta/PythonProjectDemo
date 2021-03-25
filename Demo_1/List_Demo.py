# List :- List is mutable ordered collection of elements that allows duplicate values

fruits1 = ['apple','banana','kiwi','orange','melon']
fruits2 = list(('cherry','blueberry','grapes','mango','papaya','avocado'))
List = [10,'vasanti',34,20,'datta',True]

print(fruits1)
print(fruits2)

#This statement returns all the items from the List

print(List)

# This statement returns the type of collection 

print(type(fruits1))

# This statement returns the number of items from the fruits2 list 

print(len(fruits2))

''' Accessing the items based on their index value
 this statement returns the first item from the list,first item's index will be zero'''
print(fruits1[0])

# this statement returns 5th item from the list
print(fruits2[4])

''' Negative indexing returns the items starting from last
 this statement returns the third item from the last from the list'''
print(fruits2[-2])

# This statement returns 2nd and third items
print(fruits1[1:4])

''' Negative range of indexes
 this statement returns 2nd and 3rd items from the last'''
print(fruits2[-4:-1])

# This statement returns the last two items from the list
print(List[-2:])

''' Range of indexes
 This statement returns the first four items from the list'''
print(fruits2[:4])

if "apple" in fruits1:
    
    print("yes,'apple' is there in fruits2 list")
    
if 'mango' in fruits2:
    
    print("yes,'mango' is there in fruits2 list")
    
i=0

while i < len(fruits1):
    
    print(fruits1[i])
    i=i+1
    
fruits1.insert(2,"gauva")

print(fruits1)  
  
    
    
           








