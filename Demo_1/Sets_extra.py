'''
Created on Jan 17, 2021

@author: kulkarnivasanti
'''

set = {'pink','blue','white','red','gray','black','purple'}
set1 = {}
list = []

for x in set:
    if "e" in x:
        list.append(x)

print(list)        
    
for x in set:
    print(x)   
    
set.add("orange")    
print(set) 


