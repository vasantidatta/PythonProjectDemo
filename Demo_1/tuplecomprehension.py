

colors = ('white','pink','gray','blue','yellow','orange','red')
newcolors = []
newcolors1 = []

colors1 = list(colors)

for x in colors1:
    if 'e' in x:
        newcolors.append(x)

print(newcolors)
colors = tuple(newcolors)

print(colors)

for y in colors1:
    if 'r' in y:
        newcolors1.append(y)
print(newcolors1)
        
colors = tuple(newcolors1)   

print(colors)     
        


        
        