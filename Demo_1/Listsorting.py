# list sorting in ascending and descending order

Colors = ['black','grey','orange','purple','yellow','blue','red']
Numbers = [50,60,65,44,45,38,76]
num=[]

Colors.sort()
print(Colors)

Colors.sort(reverse=True)
print(Colors)

for x in Numbers:
    if x<=50:
        num.append(x)
        num.reverse()
print("numbers less than 50 ;-",num)
        

def function(n):
    return (n-50)

Numbers.sort(key=function)
print("numbers less than 50 ->",Numbers)

    