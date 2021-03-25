set1 = {'arti','bharti','keerti','murti','spoorti','arundhati'}
set2 = {'amarsh','bhavesh','ramesh','satish','umesh'}
list = []
list1 = []
set3 = {'datta','vasanti'}
for x in set1:
    if "a" in x:
        list.append(x)
print(list)  

set2.update(list)
print(set2)

for x in set2:
    if 'e' in x:
        list1.append(x)
print(x)

set3.update(list1)
print(set3)


for x in set3:
    if 'a' in x:
        list.append(x)
print(list)   

set3.update(list)
print(set3)     


        





      
        