# Tuple :--> is immutable ordered collection of items that allows duplicates.

# Accessing tuples

Names = ("vihan","datta","mohan","satish","vignesh","jignesh")
Bnames = list(Names)
Bnames[1]="sameer"
Names = tuple(Bnames)
Names1 = []
print("New list = ",Names)

x= list(Names)
x.append("datta")
Names = tuple(x)
print("Another tuple is = ",Names)

y = list(Names)
y.remove("sameer")
Names = tuple(x)
print("Another new tuple is = ",Names)


for i in Names:
    print(i)

for x in Names:
    if 'a' in x:
        Names1.append(x)

print(Names1)        
            


    



