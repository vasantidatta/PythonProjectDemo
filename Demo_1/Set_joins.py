'''
Created on Jan 17, 2021

@author: kulkarnivasanti
'''

set1 = {'jasmin','lily','rose','lotus','marigold','hibiscus'}
set2 = {'water','rose','lamp','lotus','bell'}

""" union():-> This method will return a new set with common
               items from two or more sets"""
               
#set3 = set1.union(set2)
#print(set3)

""" update():-> This method inserts all the items from one set
                into another set"""

#set1.update(set2)
#print(set1)         

""" intersection_update():-> This method keeps the commom items from
                            two or more sets"""     

set1.intersection_update(set2)
print(set1)   

""" intersection():-> This method returns a new set with common items"""
set3 = set1.intersection(set2)
print(set3)

"""symmetric_difference_update:-> This method keeps the uncommom items 
                                from both the sets"""
set1.symmetric_difference_update(set2)
print(set1)  

set2.symmetric_difference_update(set1)
print(set2)    

"""symmetric_difference():-> This method returns a new set with uncommon items 
                             from two or more sets"""
set4 = set1.symmetric_difference(set2)
print(set4)    

set5 = set2.symmetric_difference(set1)
print(set5)                                                                                             