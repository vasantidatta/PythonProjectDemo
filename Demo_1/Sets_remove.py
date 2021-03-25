'''
Created on Jan 17, 2021

@author: kulkarnivasanti
'''

set1 = {'arti','bharti','keerti','murti','spoorti','arundhati'}
set2 = {'amaresh','bhavesh','ramesh','satish','umesh'}

set1.remove("keerti")
print(set1)

set1.discard("kruti")
print(set1)

"""set1.remove("kruti")
print(set1)"""

set1.pop()
print(set1)

set2.pop()
print(set2)

set2.clear()
print(set2)

"""del set1
print(set1)"""

set2.discard("kantesh")
print(set2)

"""set2.remove("kantesh")
print(set2)"""

set1.remove("bharti")
print(set1)
