

colors = ('white','pink','gray','blue','yellow','orange','red')
colors2 = ('black','cream','ivory','maroon','pink','orange','pink','orange')
numbers = (45,55,65,35,25,15,75,70,50,60,35,45,30,35)
newcolors = []
newnumbers = []
newnumbers1 = []
numbers2 = []


i = 0
while i<= len(colors):
    print(i)
    i = i  + 1
 
mycolors = list(colors)
mycolors.append('purple')
mycolors.remove('white')
mycolors[2] = 'silver'
colors = tuple(mycolors)

print(colors)

for x in numbers:
    if x<=50:
        newnumbers.append(x)

print(newnumbers)   

newnumbers = list(numbers)
newnumbers.sort()
numbers = tuple(newnumbers)
print(numbers)

for y in numbers:
    if y>=50:
        newnumbers1.append(y)
        
print(newnumbers1)    

for x in numbers:
    if x<=60:
        print(x)

morecolors = list(colors)
morecolors.sort()
colors = tuple(morecolors)   

print(colors) 

colors3 = colors+colors2

print(colors3)

cool = list(colors3)
cool.sort()
colors3 = tuple(cool)

print(colors3)

p = numbers.count(35)
print(p)

a = numbers.count(45)
print(a)

b = colors3.count("pink")
print(b)

c= colors3.count("orange")
print(c)

             


    