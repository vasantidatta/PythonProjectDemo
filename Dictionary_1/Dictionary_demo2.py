'''
Created on Jan 18, 2021

@author: kulkarnivasanti
'''
dict1 = {"fname":"vasanti",
         "lname":"kulkarni",
         "mname":"Datta",
         "relegion":"Hindu",
         "country":"India",
         "native":"bijapur",}
         

print(dict1)

print(dict1["fname"])

print(dict1.get("lname","mname"))

print(dict1.keys())

print(dict1.values())

print(type(dict1))

print(len(dict1))

dict1["school"] = "PDJ"

print(dict1)

print(dict1.keys())

print(dict1.values())

print(dict1.items())

dict1["college"] = "KCP Science college"

print(dict1)

print(dict1.keys())

print(dict1.values())

print(dict1.items())

''' items() method will return all the items from the dictionary
            as a tuple '''
print(dict1.items())  

for x in dict1:
    if "native" in x:
        print("yes, native is present")          


for x in dict1:
    if "lname" in x:
        print("yes, last name is present")

for x in dict1:
    if "relegion" in x:
        print("yes, relegion as Hindu is present in dict1")    
        
if 'mname' in dict1:
    print("yes, middle name is present")            

