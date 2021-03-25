'''
Created on Jan 18, 2021

@author: kulkarnivasanti
'''

dict = {'book':'ramayana','author':'valmiki','edition':'4th','pages':408}

''' ***Access the dictionary items methods***'''

print(dict["book"])

''' when user trying to access the key that is not present in the dictionary
    then below code throws an error'''
#print(dict["name"])

'''by using get() method to access the item that is not present 
   in the dictionary then below code won't throw any exception'''
print(dict.get("name"))

print(dict["author"])

''' key() method will return all the keys present in the dictionary'''
print(dict.keys())

'''values() method will return all the values present in the dictionary'''
print(dict.values())

''' items() method will dispaly all the list items as key value pairs'''
print(dict.items())

print(dict)

print(type(dict))

print(len(dict))

if 'book' in dict:
    print("yes, book is present ")
    
'''*** updating the dictionary items***'''
    
dict["publisher"] = "bharat publications"  
print(dict)      

''' using update() method also we can add the new key value pair to the 
    dictionary'''
dict.update({"year":1997}) 
print(dict)  

''' we can even replace the value by using the update method'''

dict.update({"year":2000})

print(dict["year"])
    

