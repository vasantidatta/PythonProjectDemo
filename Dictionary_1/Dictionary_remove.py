'''
Created on Jan 19, 2021

@author: kulkarnivasanti
'''

'''***removing the dictionary items using different methods***'''

dict = {'fname':'vasanti','lname':'kulkarni','rollno':82,'division':'c'}

''' pop() method removes the item specified by the key name'''
#dict.pop("division")
print(dict)

'''popitem() method removes the last inserted item'''
dict.popitem()
print(dict)

'''del keyword removes the item specified by the key name'''
del dict["rollno"]
print(dict)

''' del keyword can also delete the whole dictionary completely'''

#del dict
#print(dict)

''' clear() method removes all the items from the dictionary leaving it empty'''

dict.clear()
print(dict)